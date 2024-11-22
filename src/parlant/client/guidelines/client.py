# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guideline_list_result import GuidelineListResult
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.guideline_invoice import GuidelineInvoice
from ..types.guideline_creation_result import GuidelineCreationResult
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.guideline_with_connections_and_tool_associations import (
    GuidelineWithConnectionsAndToolAssociations,
)
from ..types.guideline_connection_update_params import GuidelineConnectionUpdateParams
from ..types.guideline_tool_association_update_params import (
    GuidelineToolAssociationUpdateParams,
)
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GuidelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuidelineListResult:
        """
        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineListResult
            Successful Response

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.list(
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineListResult,
                    parse_obj_as(
                        type_=GuidelineListResult,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        agent_id: str,
        *,
        invoices: typing.Sequence[GuidelineInvoice],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineCreationResult:
        """
        Parameters
        ----------
        agent_id : str

        invoices : typing.Sequence[GuidelineInvoice]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineCreationResult
            Successful Response

        Examples
        --------
        from parlant.client import (
            CoherenceCheck,
            GuidelineContent,
            GuidelineInvoice,
            GuidelineInvoiceData,
            GuidelinePayload,
            ParlantClient,
        )

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.create(
            agent_id="agent_id",
            invoices=[
                GuidelineInvoice(
                    payload=GuidelinePayload(
                        content=GuidelineContent(
                            condition="condition",
                            action="action",
                        ),
                        operation="add",
                        coherence_check=True,
                        connection_proposition=True,
                    ),
                    checksum="checksum",
                    approved=True,
                    data=GuidelineInvoiceData(
                        coherence_checks=[
                            CoherenceCheck(
                                kind="contradiction_with_existing_guideline",
                                first=GuidelineContent(
                                    condition="condition",
                                    action="action",
                                ),
                                second=GuidelineContent(
                                    condition="condition",
                                    action="action",
                                ),
                                issue="issue",
                                severity=1,
                            )
                        ],
                    ),
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines",
            method="POST",
            json={
                "invoices": convert_and_respect_annotation_metadata(
                    object_=invoices,
                    annotation=typing.Sequence[GuidelineInvoice],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineCreationResult,
                    parse_obj_as(
                        type_=GuidelineCreationResult,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
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
        agent_id: str,
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Parameters
        ----------
        agent_id : str

        guideline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Successful Response

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.retrieve(
            agent_id="agent_id",
            guideline_id="guideline_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines/{jsonable_encoder(guideline_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineWithConnectionsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithConnectionsAndToolAssociations,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self,
        agent_id: str,
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        agent_id : str

        guideline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.delete(
            agent_id="agent_id",
            guideline_id="guideline_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines/{jsonable_encoder(guideline_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        agent_id: str,
        guideline_id: str,
        *,
        connections: typing.Optional[GuidelineConnectionUpdateParams] = OMIT,
        tool_associations: typing.Optional[GuidelineToolAssociationUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Parameters
        ----------
        agent_id : str

        guideline_id : str

        connections : typing.Optional[GuidelineConnectionUpdateParams]

        tool_associations : typing.Optional[GuidelineToolAssociationUpdateParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Successful Response

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.update(
            agent_id="agent_id",
            guideline_id="guideline_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines/{jsonable_encoder(guideline_id)}",
            method="PATCH",
            json={
                "connections": convert_and_respect_annotation_metadata(
                    object_=connections,
                    annotation=GuidelineConnectionUpdateParams,
                    direction="write",
                ),
                "tool_associations": convert_and_respect_annotation_metadata(
                    object_=tool_associations,
                    annotation=GuidelineToolAssociationUpdateParams,
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineWithConnectionsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithConnectionsAndToolAssociations,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGuidelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuidelineListResult:
        """
        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineListResult
            Successful Response

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineListResult,
                    parse_obj_as(
                        type_=GuidelineListResult,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        agent_id: str,
        *,
        invoices: typing.Sequence[GuidelineInvoice],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineCreationResult:
        """
        Parameters
        ----------
        agent_id : str

        invoices : typing.Sequence[GuidelineInvoice]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineCreationResult
            Successful Response

        Examples
        --------
        import asyncio

        from parlant.client import (
            AsyncParlantClient,
            CoherenceCheck,
            GuidelineContent,
            GuidelineInvoice,
            GuidelineInvoiceData,
            GuidelinePayload,
        )

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.create(
                agent_id="agent_id",
                invoices=[
                    GuidelineInvoice(
                        payload=GuidelinePayload(
                            content=GuidelineContent(
                                condition="condition",
                                action="action",
                            ),
                            operation="add",
                            coherence_check=True,
                            connection_proposition=True,
                        ),
                        checksum="checksum",
                        approved=True,
                        data=GuidelineInvoiceData(
                            coherence_checks=[
                                CoherenceCheck(
                                    kind="contradiction_with_existing_guideline",
                                    first=GuidelineContent(
                                        condition="condition",
                                        action="action",
                                    ),
                                    second=GuidelineContent(
                                        condition="condition",
                                        action="action",
                                    ),
                                    issue="issue",
                                    severity=1,
                                )
                            ],
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines",
            method="POST",
            json={
                "invoices": convert_and_respect_annotation_metadata(
                    object_=invoices,
                    annotation=typing.Sequence[GuidelineInvoice],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineCreationResult,
                    parse_obj_as(
                        type_=GuidelineCreationResult,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
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
        agent_id: str,
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Parameters
        ----------
        agent_id : str

        guideline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Successful Response

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.retrieve(
                agent_id="agent_id",
                guideline_id="guideline_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines/{jsonable_encoder(guideline_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineWithConnectionsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithConnectionsAndToolAssociations,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self,
        agent_id: str,
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        agent_id : str

        guideline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.delete(
                agent_id="agent_id",
                guideline_id="guideline_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines/{jsonable_encoder(guideline_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        agent_id: str,
        guideline_id: str,
        *,
        connections: typing.Optional[GuidelineConnectionUpdateParams] = OMIT,
        tool_associations: typing.Optional[GuidelineToolAssociationUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Parameters
        ----------
        agent_id : str

        guideline_id : str

        connections : typing.Optional[GuidelineConnectionUpdateParams]

        tool_associations : typing.Optional[GuidelineToolAssociationUpdateParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Successful Response

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.update(
                agent_id="agent_id",
                guideline_id="guideline_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/guidelines/{jsonable_encoder(guideline_id)}",
            method="PATCH",
            json={
                "connections": convert_and_respect_annotation_metadata(
                    object_=connections,
                    annotation=GuidelineConnectionUpdateParams,
                    direction="write",
                ),
                "tool_associations": convert_and_respect_annotation_metadata(
                    object_=tool_associations,
                    annotation=GuidelineToolAssociationUpdateParams,
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineWithConnectionsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithConnectionsAndToolAssociations,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
