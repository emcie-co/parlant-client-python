import tempfile
import time
from multiprocessing import Process
from pathlib import Path
from pytest import fixture
from typing import Any, Generator, Iterator
import uvicorn

from parlant.client import (
    Agent,
    GuidelineContent,
    GuidelinePayload,
    GuidelineToolAssociationUpdateParams,
    GuidelineWithConnectionsAndToolAssociations,
    OpenApiServiceParams,
    ParlantClient,
    Payload,
    Term,
    ToolId,
    Invoice,
)

from tests.conftest import app
from tests.test_utilities import ContextOfTest

PLUGIN_PORT = 8802
PLUGIN_ADDRESS = f"http://localhost:{PLUGIN_PORT}"


def mock_tool() -> None:
    uvicorn.run(app, port=PLUGIN_PORT)


@fixture(scope="session", autouse=True)
def setup() -> Generator[None, Any, None]:
    proc = Process(target=mock_tool)
    proc.start()
    time.sleep(1)
    yield
    proc.terminate()


@fixture
def context() -> Iterator[ContextOfTest]:
    with tempfile.TemporaryDirectory(prefix="parlant-client_test_") as home_dir:
        home_dir_path = Path(home_dir)

        yield ContextOfTest(home_dir=home_dir_path)


SERVER_PORT = 8800
SERVER_ADDRESS = f"http://localhost:{SERVER_PORT}"


# async def test_parlant_client_happy_path_with_server_and_plugin(context: ContextOfTest) -> None:
#     _server_process = await run_cli("parlant-server", "-p", str(SERVER_PORT))
#     _plugin_process = await run_cli("python", CLI_PLUGIN_PATH, str(PLUGIN_PORT))
#     try:
#         await asyncio.sleep(REASONABLE_AMOUNT_OF_TIME)
#         await _test_parlant_client_happy_path(context)
#     finally:
#         _plugin_process.kill()
#         await _plugin_process.wait()
#         _server_process.kill()
#         await _server_process.wait()


async def test_parlant_client_happy_path(context: ContextOfTest) -> None:
    client = make_parlant_client(base_url=SERVER_ADDRESS)

    agent = make_api_agent(client=client, name="demo-agent")

    guideline_randoms = make_guideline(
        client=client,
        agent_id=agent.id,
        action="Use the randoms tool to either flip coins or roll dice.",
        condition="The users wants a random number.",
    )
    assert guideline_randoms

    _term = make_term(
        client=client,
        agent_id=agent.id,
        name="Melupapepkin",
        description="A word that's meaning should be ignored. Serves as an arbitrary identifier.",
        synonyms=["Shoshanna", "Moshe"],
    )
    assert _term

    make_service_tool_association(
        client=client,
        agent_id=agent.id,
        guideline_id=guideline_randoms.guideline.id,
        tool_name="randoms",
        service_url=PLUGIN_ADDRESS,
    )

    session = client.sessions.create(
        agent_id=agent.id,
    )
    assert session

    event = client.sessions.create_event(
        session.id,
        kind="message",
        source="customer",
        message="Heads or tails?",
        moderation="auto",
    )
    assert event

    event_inspection_result = client.sessions.inspect_event(
        session.id,
        event.id,
    )

    assert event_inspection_result
    print(event_inspection_result)

    events = client.sessions.list_events(
        session.id, min_offset=event_inspection_result.event.offset + 1
    )
    assert events
    for event in events:
        print(event)
        assert event


def make_parlant_client(base_url: str) -> ParlantClient:
    client = ParlantClient(base_url=base_url)
    print(f"ParlantClient created with server=`{base_url}`.")
    return client


def make_api_agent(client: ParlantClient, name: str) -> Agent:
    agent = client.agents.create(name=name)
    print(f"Agent `{name}` created.")
    return agent


def make_guideline_evaluation(
    client: ParlantClient,
    agent_id: str,
    action: str,
    condition: str,
) -> str:
    guideline_payload = GuidelinePayload(
        coherence_check=True,
        connection_proposition=True,
        content=GuidelineContent(action=action, condition=condition),
        operation="add",
    )

    create_evaluation_response = client.evaluations.create(
        agent_id=agent_id,
        payloads=[Payload(kind="guideline", guideline=guideline_payload)],
    )
    print(f"Evaluation created with id=`{create_evaluation_response.id}`")
    return create_evaluation_response.id


def make_guideline(
    client: ParlantClient,
    agent_id: str,
    action: str,
    condition: str,
) -> GuidelineWithConnectionsAndToolAssociations:
    evaluation_id = make_guideline_evaluation(
        client=client,
        agent_id=agent_id,
        action=action,
        condition=condition,
    )

    while True:
        read_evaluation_response = client.evaluations.retrieve(evaluation_id=evaluation_id)

        if read_evaluation_response.status == "running":
            time.sleep(1)
            continue

        if read_evaluation_response.status != "completed":
            raise Exception(read_evaluation_response.status)

        guidelines_invoices: list[Invoice] = []

        for invoice in read_evaluation_response.invoices:
            if not invoice.data or not invoice.payload.guideline or not invoice.data.guideline:
                continue

            guidelines_invoices.append(
                Invoice(
                    payload=invoice.payload,
                    checksum=invoice.checksum,
                    approved=invoice.approved,
                    data=invoice.data,
                    error=invoice.error,
                ),
            )

        guidelines_create_response = client.guidelines.create(
            agent_id,
            invoices=guidelines_invoices,
        )
        print(f"Created Guideline item=`{guidelines_create_response.items[0]}`")
        return guidelines_create_response.items[0]


def make_term(
    client: ParlantClient,
    agent_id: str,
    name: str,
    description: str,
    synonyms: list[str] | None,
) -> Term:
    term = client.glossary.create_term(
        agent_id=agent_id, name=name, description=description, synonyms=synonyms
    )
    print(f"Created Term `{name}~{synonyms}`='{description}'")
    return term


def make_service_tool_association(
    client: ParlantClient,
    agent_id: str,
    guideline_id: str,
    tool_name: str,
    service_url: str,
) -> None:
    _create_service_response = client.services.create_or_update(
        tool_name,
        kind="openapi",
        openapi=OpenApiServiceParams(
            url=PLUGIN_ADDRESS,
            source=f"{PLUGIN_ADDRESS}/openapi.json",
        ),
    )
    service = client.services.retrieve(tool_name)
    assert service.tools
    tool_randoms_flip = service.tools[0]
    tool_randoms_roll = service.tools[1]
    print("Got tools from service.")
    _ = client.guidelines.update(
        agent_id,
        guideline_id,
        tool_associations=GuidelineToolAssociationUpdateParams(
            add=[
                ToolId(service_name=service.name, tool_name=tool_randoms_flip.name),
                ToolId(service_name=service.name, tool_name=tool_randoms_roll.name),
            ]
        ),
    )
    print("Patched guideline with relevant tools.")
