import time

from parlant.client import ParlantClient
from parlant.client.types.agent import Agent # OR from parlant.client import Agent
from parlant.client.types.create_agent_request import CreateAgentRequest
from parlant.client.types.guideline_content import GuidelineContent
from parlant.client.types.guideline_invoice import GuidelineInvoice
from parlant.client.types.guideline_payload import GuidelinePayload
from parlant.client.types.guideline_tool_associations_patch import (
    GuidelineToolAssociationsPatch,
)
from parlant.client.types.guideline_with_connections_and_tool_associations import (
    GuidelineWithConnectionsAndToolAssociations,
)
from parlant.client.types.request import Request_Sdk
from parlant.client.types.term import Term

from parlant.client.types.tool_id import ToolId


def make_parlant_client(base_url: str) -> ParlantClient:
    client = ParlantClient(base_url=base_url)
    print(f"ParlantClient with server=`{base_url}` created.")
    return client


def make_api_agent(client: ParlantClient, name: str) -> Agent:
    create_agent_request = CreateAgentRequest(name=name)
    create_agent_reponse = client.create_agent(request=create_agent_request)
    print(f"Agent `{name}` created.")
    return create_agent_reponse.agent


def make_guideline_evaluation(
    client: ParlantClient,
    agent_id: str,
    action: str,
    predicate: str,
) -> str:
    guideline_payload = GuidelinePayload(
        coherence_check=True,
        connection_proposition=True,
        content=GuidelineContent(action=action, predicate=predicate),
        kind="guideline",
        operation="add",
    )

    create_evaluation_response = client.create_evaluation(
        agent_id=agent_id,
        payloads=[guideline_payload],
    )
    print(f"Evaluation created with id=`{create_evaluation_response.evaluation_id}`")
    return create_evaluation_response.evaluation_id


def make_guideline(
    client: ParlantClient,
    agent_id: str,
    action: str,
    predicate: str,
) -> GuidelineWithConnectionsAndToolAssociations:
    evaluation_id = make_guideline_evaluation(
        client=client, agent_id=agent_id, action=action, predicate=predicate
    )

    while True:
        read_evaluation_response = client.read_evaluation(evaluation_id=evaluation_id)

        if read_evaluation_response.status == "running":
            time.sleep(1)
            continue

        if read_evaluation_response.status != "completed":
            raise Exception(read_evaluation_response.status)

        guidelines_invoices: list[GuidelineInvoice] = []

        for invoice in read_evaluation_response.invoices:
            if invoice.data is None:
                continue
            guidelines_invoices.append(
                GuidelineInvoice(
                    payload=invoice.payload,
                    checksum=invoice.checksum,
                    approved=invoice.approved,
                    data=invoice.data,
                    error=invoice.error,
                ),
            )

        guidelines_create_response = client.create_guidelines(
            agent.id,
            invoices=guidelines_invoices,
        )
        print(f"Created Guideline item=`{guidelines_create_response.items[0]}`")
        return guidelines_create_response.items[0]


def make_term(
    client: ParlantClient, agent_id: str, name: str, description: str, synonyms: list[str] | None
) -> Term:
    create_term_response = client.create_term(
        agent_id=agent_id, name=name, description=description, synonyms=synonyms
    )
    print(f"Created Term `{name}~{synonyms}`='{description}'")
    return create_term_response.term


def associate_service_tool(guideline_id: str, tool_name: str, tool_url: str):
    _create_service_response = client.upsert_service(tool_name, request=Request_Sdk(url=tool_url))
    service = client.read_service(tool_name)
    assert service.tools
    tool_randoms_flip = service.tools[1]
    tool_randoms_roll = service.tools[2]
    print("Got tools from service.")
    _patch_guildeline_reponse = client.patch_guideline(
        agent.id,
        guideline_id,
        tool_associations=GuidelineToolAssociationsPatch(
            add=[
                ToolId(service_name=service.name, tool_name=tool_randoms_flip.name),
                ToolId(service_name=service.name, tool_name=tool_randoms_roll.name),
            ]
        ),
    )
    print("Patched guideline with relevant tools.")


if __name__ == "__main__":
    # Strictly Happy Path
    client = make_parlant_client(base_url="http://127.0.0.1:8000")

    agent = make_api_agent(client=client, name="demo-agent")

    guideline_randoms = make_guideline(
        client=client,
        agent_id=agent.id,
        action="Use the randoms tool to either flip coins or roll dice.",
        predicate="The users wants a random number.",
    )

    make_term(
        client=client,
        agent_id=agent.id,
        name="Melupapepkin",
        description="A word that's meaning should be ignored. Serves as an arbitrary identifier.",
        synonyms=["Shoshanna", "Moshe"],
    )

    associate_service_tool(
        guideline_randoms.guideline.id,
        "randoms",
        "http://host.docker.internal:8009",
    )

    create_session_response = client.create_session(
        end_user_id="end_user",
        agent_id=agent.id,
    )
    demo_session = create_session_response.session

    create_event_response = client.create_event(
        demo_session.id,
        kind="message",
        source="end_user",
        content="Heads or tails?",
        moderation="auto",
    )
    # event_source = create_event_response.event.source

    print("---\nThe user asks: Heads or tails?\n")

    last_known_offset = user_message_offset = create_event_response.event.offset
    list_interaction_response = client.list_interactions(
        demo_session.id, min_event_offset=last_known_offset, source="ai_agent", wait=True
    )

    print("---\nThe agent responds:\n")

    for interaction in list_interaction_response.interactions:
        print(interaction.data)


print("\n=== FIN ===\n")
