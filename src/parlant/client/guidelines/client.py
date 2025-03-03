# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guideline import Guideline
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.guideline_with_connections_and_tool_associations import (
    GuidelineWithConnectionsAndToolAssociations,
)
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..types.guideline_connection_update_params import GuidelineConnectionUpdateParams
from ..types.guideline_tool_association_update_params import (
    GuidelineToolAssociationUpdateParams,
)
from ..types.guideline_tags_update_params import GuidelineTagsUpdateParams
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GuidelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        tag_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Guideline]:
        """
        Lists all guidelines for the specified tag or all guidelines if no tag is provided.

        Returns an empty list if no guidelines exist.
        Guidelines are returned in no guaranteed order.
        Does not include connections or tool associations.

        Parameters
        ----------
        tag_id : typing.Optional[str]
            The tag ID to filter guidelines by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Guideline]
            List of all guidelines for the specified tag or all guidelines if no tag is provided

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "guidelines",
            method="GET",
            params={
                "tag_id": tag_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Guideline],
                    parse_obj_as(
                        type_=typing.List[Guideline],  # type: ignore
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

    def create(
        self,
        *,
        condition: str,
        action: str,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guideline:
        """
        Creates a new guideline.

        See the [documentation](https://parlant.io/docs/concepts/customization/guidelines) for more information.

        Parameters
        ----------
        condition : str
            If this condition is satisfied, the action will be performed

        action : str
            This action will be performed if the condition is satisfied

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guideline
            Guideline successfully created. Returns the created guideline.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.create(
            condition="when the customer asks about pricing",
            action="provide current pricing information and mention any ongoing promotions",
            enabled=False,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "guidelines",
            method="POST",
            json={
                "condition": condition,
                "action": action,
                "enabled": enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Guideline,
                    parse_obj_as(
                        type_=Guideline,  # type: ignore
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
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Retrieves a specific guideline with all its connections and tool associations.

        Returns both direct and indirect connections between guidelines.
        Tool associations indicate which tools the guideline can use.

        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Guideline details successfully retrieved. Returns the complete guideline with its connections and tool associations.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.retrieve(
            guideline_id="IUCGT-l4pS",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
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
        self,
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

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
            guideline_id="IUCGT-l4pS",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
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

    def update(
        self,
        guideline_id: str,
        *,
        condition: typing.Optional[str] = OMIT,
        action: typing.Optional[str] = OMIT,
        connections: typing.Optional[GuidelineConnectionUpdateParams] = OMIT,
        tool_associations: typing.Optional[GuidelineToolAssociationUpdateParams] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        tags: typing.Optional[GuidelineTagsUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Updates a guideline's connections and tool associations.

        Only provided attributes will be updated; others remain unchanged.

        Connection rules:
        - A guideline cannot connect to itself
        - Only direct connections can be removed
        - The connection must specify this guideline as source or target

        Tool Association rules:
        - Tool services and tools must exist before creating associations

        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

        condition : typing.Optional[str]
            If this condition is satisfied, the action will be performed

        action : typing.Optional[str]
            This action will be performed if the condition is satisfied

        connections : typing.Optional[GuidelineConnectionUpdateParams]

        tool_associations : typing.Optional[GuidelineToolAssociationUpdateParams]

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        tags : typing.Optional[GuidelineTagsUpdateParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Guideline successfully updated. Returns the updated guideline with its connections and tool associations.

        Examples
        --------
        from parlant.client import (
            GuidelineConnectionAddition,
            GuidelineConnectionUpdateParams,
            GuidelineToolAssociationUpdateParams,
            ParlantClient,
            ToolId,
        )

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.update(
            guideline_id="IUCGT-l4pS",
            connections=GuidelineConnectionUpdateParams(
                add=[
                    GuidelineConnectionAddition(
                        source="guide_123xyz",
                        target="guide_789xyz",
                    )
                ],
                remove=["guide_456xyz"],
            ),
            tool_associations=GuidelineToolAssociationUpdateParams(
                add=[
                    ToolId(
                        service_name="pricing_service",
                        tool_name="get_prices",
                    )
                ],
                remove=[
                    ToolId(
                        service_name="old_service",
                        tool_name="old_tool",
                    )
                ],
            ),
            enabled=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
            method="PATCH",
            json={
                "condition": condition,
                "action": action,
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
                "enabled": enabled,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags,
                    annotation=GuidelineTagsUpdateParams,
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


class AsyncGuidelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        tag_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Guideline]:
        """
        Lists all guidelines for the specified tag or all guidelines if no tag is provided.

        Returns an empty list if no guidelines exist.
        Guidelines are returned in no guaranteed order.
        Does not include connections or tool associations.

        Parameters
        ----------
        tag_id : typing.Optional[str]
            The tag ID to filter guidelines by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Guideline]
            List of all guidelines for the specified tag or all guidelines if no tag is provided

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "guidelines",
            method="GET",
            params={
                "tag_id": tag_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Guideline],
                    parse_obj_as(
                        type_=typing.List[Guideline],  # type: ignore
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

    async def create(
        self,
        *,
        condition: str,
        action: str,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guideline:
        """
        Creates a new guideline.

        See the [documentation](https://parlant.io/docs/concepts/customization/guidelines) for more information.

        Parameters
        ----------
        condition : str
            If this condition is satisfied, the action will be performed

        action : str
            This action will be performed if the condition is satisfied

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guideline
            Guideline successfully created. Returns the created guideline.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.create(
                condition="when the customer asks about pricing",
                action="provide current pricing information and mention any ongoing promotions",
                enabled=False,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "guidelines",
            method="POST",
            json={
                "condition": condition,
                "action": action,
                "enabled": enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Guideline,
                    parse_obj_as(
                        type_=Guideline,  # type: ignore
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
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Retrieves a specific guideline with all its connections and tool associations.

        Returns both direct and indirect connections between guidelines.
        Tool associations indicate which tools the guideline can use.

        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Guideline details successfully retrieved. Returns the complete guideline with its connections and tool associations.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.retrieve(
                guideline_id="IUCGT-l4pS",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
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
        self,
        guideline_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

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
                guideline_id="IUCGT-l4pS",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
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

    async def update(
        self,
        guideline_id: str,
        *,
        condition: typing.Optional[str] = OMIT,
        action: typing.Optional[str] = OMIT,
        connections: typing.Optional[GuidelineConnectionUpdateParams] = OMIT,
        tool_associations: typing.Optional[GuidelineToolAssociationUpdateParams] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        tags: typing.Optional[GuidelineTagsUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithConnectionsAndToolAssociations:
        """
        Updates a guideline's connections and tool associations.

        Only provided attributes will be updated; others remain unchanged.

        Connection rules:
        - A guideline cannot connect to itself
        - Only direct connections can be removed
        - The connection must specify this guideline as source or target

        Tool Association rules:
        - Tool services and tools must exist before creating associations

        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

        condition : typing.Optional[str]
            If this condition is satisfied, the action will be performed

        action : typing.Optional[str]
            This action will be performed if the condition is satisfied

        connections : typing.Optional[GuidelineConnectionUpdateParams]

        tool_associations : typing.Optional[GuidelineToolAssociationUpdateParams]

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        tags : typing.Optional[GuidelineTagsUpdateParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithConnectionsAndToolAssociations
            Guideline successfully updated. Returns the updated guideline with its connections and tool associations.

        Examples
        --------
        import asyncio

        from parlant.client import (
            AsyncParlantClient,
            GuidelineConnectionAddition,
            GuidelineConnectionUpdateParams,
            GuidelineToolAssociationUpdateParams,
            ToolId,
        )

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.update(
                guideline_id="IUCGT-l4pS",
                connections=GuidelineConnectionUpdateParams(
                    add=[
                        GuidelineConnectionAddition(
                            source="guide_123xyz",
                            target="guide_789xyz",
                        )
                    ],
                    remove=["guide_456xyz"],
                ),
                tool_associations=GuidelineToolAssociationUpdateParams(
                    add=[
                        ToolId(
                            service_name="pricing_service",
                            tool_name="get_prices",
                        )
                    ],
                    remove=[
                        ToolId(
                            service_name="old_service",
                            tool_name="old_tool",
                        )
                    ],
                ),
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
            method="PATCH",
            json={
                "condition": condition,
                "action": action,
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
                "enabled": enabled,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags,
                    annotation=GuidelineTagsUpdateParams,
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
