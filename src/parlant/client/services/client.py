# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service import Service
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..errors.service_unavailable_error import ServiceUnavailableError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.tool_service_kind_dto import ToolServiceKindDto
from ..types.sdk_service_params import SdkServiceParams
from ..types.open_api_service_params import OpenApiServiceParams
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Service:
        """
        Get details about a specific service including all its tools.

        The response includes:

        - Basic service information (name, kind, URL)
        - Complete list of available tools
        - Parameter definitions for each tool

        Notes:

        - Tools list may be empty if service is still initializing
        - Parameters marked as required must be provided when using a tool
        - Enum parameters restrict inputs to the listed values

        Parameters
        ----------
        name : str
            Unique identifier for the service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Service details including all available tools

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.services.retrieve(
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,  # type: ignore
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def create_or_update(
        self,
        name: str,
        *,
        kind: ToolServiceKindDto,
        sdk: typing.Optional[SdkServiceParams] = OMIT,
        openapi: typing.Optional[OpenApiServiceParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Creates a new service or updates an existing one.

        For SDK services:

        - Target server must implement the Parlant SDK protocol
        - Supports bidirectional communication and streaming

        For OpenAPI services:

        - Spec must be accessible and compatible with OpenAPI 3.0
        - Limited to request/response patterns

        Common requirements:

        - Service names must be unique and kebab-case
        - URLs must include http:// or https:// scheme
        - Updates cause brief service interruption while reconnecting

        Parameters
        ----------
        name : str
            Unique identifier for the service

        kind : ToolServiceKindDto

        sdk : typing.Optional[SdkServiceParams]
            SDK service configuration parameters. Required when kind is 'sdk'.

        openapi : typing.Optional[OpenApiServiceParams]
            OpenAPI service configuration parameters. Required when kind is 'openapi'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Service successfully created or updated. The service may take a few seconds to become fully operational as it establishes connections.

        Examples
        --------
        from parlant.client import OpenApiServiceParams, ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.services.create_or_update(
            name="name",
            kind="openapi",
            openapi=OpenApiServiceParams(
                url="https://email-service.example.com/api/v1",
                source="https://email-service.example.com/api/openapi.json",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(name)}",
            method="PUT",
            json={
                "kind": kind,
                "sdk": convert_and_respect_annotation_metadata(
                    object_=sdk, annotation=SdkServiceParams, direction="write"
                ),
                "openapi": convert_and_respect_annotation_metadata(
                    object_=openapi, annotation=OpenApiServiceParams, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a service integration.

        Effects:

        - Active connections are terminated immediately
        - Service tools become unavailable to agents
        - Historical data about tool usage is preserved
        - Running operations may fail

        Parameters
        ----------
        name : str
            Unique identifier for the service

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
        client.services.delete(
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Service]:
        """
        Returns basic info about all registered services.

        For performance reasons, tool details are omitted from the response.
        Use the retrieve endpoint to get complete information including
        tools for a specific service.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            List of all registered services. Tool lists are not
                            included for performance - use the retrieve endpoint to get tools
                            for a specific service.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.services.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Service],
                    parse_obj_as(
                        type_=typing.List[Service],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Service:
        """
        Get details about a specific service including all its tools.

        The response includes:

        - Basic service information (name, kind, URL)
        - Complete list of available tools
        - Parameter definitions for each tool

        Notes:

        - Tools list may be empty if service is still initializing
        - Parameters marked as required must be provided when using a tool
        - Enum parameters restrict inputs to the listed values

        Parameters
        ----------
        name : str
            Unique identifier for the service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Service details including all available tools

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.services.retrieve(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,  # type: ignore
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def create_or_update(
        self,
        name: str,
        *,
        kind: ToolServiceKindDto,
        sdk: typing.Optional[SdkServiceParams] = OMIT,
        openapi: typing.Optional[OpenApiServiceParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Creates a new service or updates an existing one.

        For SDK services:

        - Target server must implement the Parlant SDK protocol
        - Supports bidirectional communication and streaming

        For OpenAPI services:

        - Spec must be accessible and compatible with OpenAPI 3.0
        - Limited to request/response patterns

        Common requirements:

        - Service names must be unique and kebab-case
        - URLs must include http:// or https:// scheme
        - Updates cause brief service interruption while reconnecting

        Parameters
        ----------
        name : str
            Unique identifier for the service

        kind : ToolServiceKindDto

        sdk : typing.Optional[SdkServiceParams]
            SDK service configuration parameters. Required when kind is 'sdk'.

        openapi : typing.Optional[OpenApiServiceParams]
            OpenAPI service configuration parameters. Required when kind is 'openapi'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Service successfully created or updated. The service may take a few seconds to become fully operational as it establishes connections.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient, OpenApiServiceParams

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.services.create_or_update(
                name="name",
                kind="openapi",
                openapi=OpenApiServiceParams(
                    url="https://email-service.example.com/api/v1",
                    source="https://email-service.example.com/api/openapi.json",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(name)}",
            method="PUT",
            json={
                "kind": kind,
                "sdk": convert_and_respect_annotation_metadata(
                    object_=sdk, annotation=SdkServiceParams, direction="write"
                ),
                "openapi": convert_and_respect_annotation_metadata(
                    object_=openapi, annotation=OpenApiServiceParams, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a service integration.

        Effects:

        - Active connections are terminated immediately
        - Service tools become unavailable to agents
        - Historical data about tool usage is preserved
        - Running operations may fail

        Parameters
        ----------
        name : str
            Unique identifier for the service

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
            await client.services.delete(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Service]:
        """
        Returns basic info about all registered services.

        For performance reasons, tool details are omitted from the response.
        Use the retrieve endpoint to get complete information including
        tools for a specific service.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            List of all registered services. Tool lists are not
                            included for performance - use the retrieve endpoint to get tools
                            for a specific service.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.services.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Service],
                    parse_obj_as(
                        type_=typing.List[Service],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
