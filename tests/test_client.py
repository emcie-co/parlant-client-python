import tempfile
import time
from pathlib import Path
from pytest import fixture
from typing import Iterator

from parlant.client import (
    Agent,
    GuidelineContent,
    GuidelineInvoice,
    GuidelinePayload,
    GuidelineToolAssociationUpdateParams,
    GuidelineWithConnectionsAndToolAssociations,
    ParlantClient,
    Payload,
    SdkServiceParams,
    Term,
    ToolId,
)

from example_plugin import (
    PLUGIN_ADDRESS,
)
from test_utilities import ContextOfTest


@fixture
def context() -> Iterator[ContextOfTest]:
    with tempfile.TemporaryDirectory(prefix="parlant-client_test_") as home_dir:
        home_dir_path = Path(home_dir)

        yield ContextOfTest(home_dir=home_dir_path)


REASONABLE_AMOUNT_OF_TIME = 15
SERVER_PORT = 8012
SERVER_ADDRESS = f"http://localhost:{SERVER_PORT}"
CLI_PLUGIN_PATH = "tests/example_plugin.py"


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

    create_session_response = client.sessions.create(
        end_user_id="end_user",
        agent_id=agent.id,
    )
    assert create_session_response
    demo_session = create_session_response.session

    create_event_response = client.sessions.create_event(
        demo_session.id,
        kind="message",
        source="end_user",
        content="Heads or tails?",
        moderation="auto",
    )
    assert create_event_response

    last_known_offset = create_event_response.event.offset
    list_interaction_response = client.sessions.list_interactions(
        demo_session.id,
        min_event_offset=last_known_offset,
        source="ai_agent",
        wait=True,
    )

    for interaction in list_interaction_response.interactions:
        assert interaction.data
        print(interaction.data)


def make_parlant_client(base_url: str) -> ParlantClient:
    client = ParlantClient(base_url=base_url)
    print(f"ParlantClient created with server=`{base_url}`.")
    return client


def make_api_agent(client: ParlantClient, name: str) -> Agent:
    create_agent_reponse = client.agents.create(name=name)
    print(f"Agent `{name}` created.")
    return create_agent_reponse.agent


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
    print(f"Evaluation created with id=`{create_evaluation_response.evaluation_id}`")
    return create_evaluation_response.evaluation_id


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

        guidelines_invoices: list[GuidelineInvoice] = []

        for invoice in read_evaluation_response.invoices:
            if not invoice.data or not invoice.payload.guideline or not invoice.data.guideline:
                continue

            guidelines_invoices.append(
                GuidelineInvoice(
                    payload=invoice.payload.guideline,
                    checksum=invoice.checksum,
                    approved=invoice.approved,
                    data=invoice.data.guideline,
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
    create_term_response = client.glossary.create_term(
        agent_id=agent_id, name=name, description=description, synonyms=synonyms
    )
    print(f"Created Term `{name}~{synonyms}`='{description}'")
    return create_term_response.term


def make_service_tool_association(
    client: ParlantClient,
    agent_id: str,
    guideline_id: str,
    tool_name: str,
    service_url: str,
) -> None:
    _create_service_response = client.services.create_or_update(
        tool_name,
        kind="sdk",
        sdk=SdkServiceParams(url=service_url),
    )
    service = client.services.retrieve(tool_name)
    assert service.tools
    tool_randoms_flip = service.tools[1]
    tool_randoms_roll = service.tools[2]
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
