# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.payload import Payload
from ..core.request_options import RequestOptions
from ..types.evaluation import Evaluation
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EvaluationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        agent_id: str,
        payloads: typing.Sequence[Payload],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Evaluation:
        """
        Creates a new evaluation task for the specified agent.

        An evaluation analyzes proposed changes (payloads) to an agent's guidelines
        to ensure coherence and consistency with existing guidelines and the agent's
        configuration. This helps maintain predictable agent behavior by detecting
        potential conflicts and unintended consequences before applying changes.

        Returns immediately with the created evaluation's initial state.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent

        payloads : typing.Sequence[Payload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Evaluation
            Evaluation successfully created. Returns the initial evaluation state.

        Examples
        --------
        from parlant.client import GuidelineContent, GuidelinePayload, ParlantClient, Payload

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluations.create(
            agent_id="a1g2e3n4t5",
            payloads=[
                Payload(
                    guideline=GuidelinePayload(
                        content=GuidelineContent(
                            condition="when customer asks about pricing",
                            action="provide current pricing information",
                        ),
                        operation="add",
                        coherence_check=True,
                        connection_proposition=True,
                    ),
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "index/evaluations",
            method="POST",
            json={
                "agent_id": agent_id,
                "payloads": convert_and_respect_annotation_metadata(
                    object_=payloads,
                    annotation=typing.Sequence[Payload],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Evaluation,
                    parse_obj_as(
                        type_=Evaluation,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        evaluation_id: str,
        *,
        wait_for_completion: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Evaluation:
        """
        Retrieves the current state of an evaluation.

        - If wait_for_completion == 0, returns current state immediately.
        - If wait_for_completion > 0, waits for completion/failure or timeout. Defaults to 60.

        Notes:
        When wait_for_completion > 0:

        - Returns final state if evaluation completes within timeout
        - Raises 504 if timeout is reached before completion

        Parameters
        ----------
        evaluation_id : str
            Unique identifier of the evaluation to retrieve

        wait_for_completion : typing.Optional[int]
            Maximum time in seconds to wait for evaluation completion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Evaluation
            Evaluation details successfully retrieved.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluations.retrieve(
            evaluation_id="evaluation_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"index/evaluations/{jsonable_encoder(evaluation_id)}",
            method="GET",
            params={
                "wait_for_completion": wait_for_completion,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Evaluation,
                    parse_obj_as(
                        type_=Evaluation,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEvaluationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        agent_id: str,
        payloads: typing.Sequence[Payload],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Evaluation:
        """
        Creates a new evaluation task for the specified agent.

        An evaluation analyzes proposed changes (payloads) to an agent's guidelines
        to ensure coherence and consistency with existing guidelines and the agent's
        configuration. This helps maintain predictable agent behavior by detecting
        potential conflicts and unintended consequences before applying changes.

        Returns immediately with the created evaluation's initial state.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent

        payloads : typing.Sequence[Payload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Evaluation
            Evaluation successfully created. Returns the initial evaluation state.

        Examples
        --------
        import asyncio

        from parlant.client import (
            AsyncParlantClient,
            GuidelineContent,
            GuidelinePayload,
            Payload,
        )

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.evaluations.create(
                agent_id="a1g2e3n4t5",
                payloads=[
                    Payload(
                        guideline=GuidelinePayload(
                            content=GuidelineContent(
                                condition="when customer asks about pricing",
                                action="provide current pricing information",
                            ),
                            operation="add",
                            coherence_check=True,
                            connection_proposition=True,
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "index/evaluations",
            method="POST",
            json={
                "agent_id": agent_id,
                "payloads": convert_and_respect_annotation_metadata(
                    object_=payloads,
                    annotation=typing.Sequence[Payload],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Evaluation,
                    parse_obj_as(
                        type_=Evaluation,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        evaluation_id: str,
        *,
        wait_for_completion: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Evaluation:
        """
        Retrieves the current state of an evaluation.

        - If wait_for_completion == 0, returns current state immediately.
        - If wait_for_completion > 0, waits for completion/failure or timeout. Defaults to 60.

        Notes:
        When wait_for_completion > 0:

        - Returns final state if evaluation completes within timeout
        - Raises 504 if timeout is reached before completion

        Parameters
        ----------
        evaluation_id : str
            Unique identifier of the evaluation to retrieve

        wait_for_completion : typing.Optional[int]
            Maximum time in seconds to wait for evaluation completion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Evaluation
            Evaluation details successfully retrieved.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.evaluations.retrieve(
                evaluation_id="evaluation_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"index/evaluations/{jsonable_encoder(evaluation_id)}",
            method="GET",
            params={
                "wait_for_completion": wait_for_completion,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Evaluation,
                    parse_obj_as(
                        type_=Evaluation,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
