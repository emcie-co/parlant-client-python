# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guideline import Guideline
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.guideline_with_relationships_and_tool_associations import (
    GuidelineWithRelationshipsAndToolAssociations,
)
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..types.guideline_relationship_update_params import (
    GuidelineRelationshipUpdateParams,
)
from ..types.guideline_tool_association_update_params import (
    GuidelineToolAssociationUpdateParams,
)
from ..types.guideline_tags_update_params import GuidelineTagsUpdateParams
from ..types.guideline_metadata_update_params import GuidelineMetadataUpdateParams
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
        Does not include relationships or tool associations.

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Metadata for the guideline

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the guideline

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
            metadata={"key1": "value1", "key2": "value2"},
            enabled=False,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "guidelines",
            method="POST",
            json={
                "condition": condition,
                "action": action,
                "metadata": metadata,
                "enabled": enabled,
                "tags": tags,
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
    ) -> GuidelineWithRelationshipsAndToolAssociations:
        """
        Retrieves a specific guideline with all its relationships and tool associations.

        Returns both direct and indirect relationships between guidelines.
        Tool associations indicate which tools the guideline can use.

        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithRelationshipsAndToolAssociations
            Guideline details successfully retrieved. Returns the complete guideline with its relationships and tool associations.

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
                    GuidelineWithRelationshipsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithRelationshipsAndToolAssociations,  # type: ignore
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
        relationships: typing.Optional[GuidelineRelationshipUpdateParams] = OMIT,
        tool_associations: typing.Optional[GuidelineToolAssociationUpdateParams] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        tags: typing.Optional[GuidelineTagsUpdateParams] = OMIT,
        metadata: typing.Optional[GuidelineMetadataUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithRelationshipsAndToolAssociations:
        """
        Updates a guideline's relationships and tool associations.

        Only provided attributes will be updated; others remain unchanged.

        Relationship rules:
        - A guideline cannot relate to itself
        - Only direct relationships can be removed
        - The relationship must specify this guideline as source or target

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

        relationships : typing.Optional[GuidelineRelationshipUpdateParams]

        tool_associations : typing.Optional[GuidelineToolAssociationUpdateParams]

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        tags : typing.Optional[GuidelineTagsUpdateParams]

        metadata : typing.Optional[GuidelineMetadataUpdateParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithRelationshipsAndToolAssociations
            Guideline successfully updated. Returns the updated guideline with its relationships and tool associations.

        Examples
        --------
        from parlant.client import (
            GuidelineMetadataUpdateParams,
            GuidelineRelationshipAddition,
            GuidelineRelationshipUpdateParams,
            GuidelineToolAssociationUpdateParams,
            ParlantClient,
            ToolId,
        )

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.guidelines.update(
            guideline_id="IUCGT-l4pS",
            condition="when the customer asks about pricing",
            action="provide current pricing information",
            relationships=GuidelineRelationshipUpdateParams(
                add=[
                    GuidelineRelationshipAddition(
                        kind="entailment",
                    )
                ],
                remove=["guideline_relationship_id_789yz"],
            ),
            tool_associations=GuidelineToolAssociationUpdateParams(
                add=[
                    ToolId(
                        service_name="new_service",
                        tool_name="new_tool",
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
            metadata=GuidelineMetadataUpdateParams(
                add={"key1": "value1", "key2": "value2"},
                remove=["key3", "key4"],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
            method="PATCH",
            json={
                "condition": condition,
                "action": action,
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships,
                    annotation=GuidelineRelationshipUpdateParams,
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
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata,
                    annotation=GuidelineMetadataUpdateParams,
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineWithRelationshipsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithRelationshipsAndToolAssociations,  # type: ignore
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
        Does not include relationships or tool associations.

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Metadata for the guideline

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the guideline

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
                metadata={"key1": "value1", "key2": "value2"},
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
                "metadata": metadata,
                "enabled": enabled,
                "tags": tags,
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
    ) -> GuidelineWithRelationshipsAndToolAssociations:
        """
        Retrieves a specific guideline with all its relationships and tool associations.

        Returns both direct and indirect relationships between guidelines.
        Tool associations indicate which tools the guideline can use.

        Parameters
        ----------
        guideline_id : str
            Unique identifier for the guideline

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithRelationshipsAndToolAssociations
            Guideline details successfully retrieved. Returns the complete guideline with its relationships and tool associations.

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
                    GuidelineWithRelationshipsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithRelationshipsAndToolAssociations,  # type: ignore
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
        relationships: typing.Optional[GuidelineRelationshipUpdateParams] = OMIT,
        tool_associations: typing.Optional[GuidelineToolAssociationUpdateParams] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        tags: typing.Optional[GuidelineTagsUpdateParams] = OMIT,
        metadata: typing.Optional[GuidelineMetadataUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuidelineWithRelationshipsAndToolAssociations:
        """
        Updates a guideline's relationships and tool associations.

        Only provided attributes will be updated; others remain unchanged.

        Relationship rules:
        - A guideline cannot relate to itself
        - Only direct relationships can be removed
        - The relationship must specify this guideline as source or target

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

        relationships : typing.Optional[GuidelineRelationshipUpdateParams]

        tool_associations : typing.Optional[GuidelineToolAssociationUpdateParams]

        enabled : typing.Optional[bool]
            Whether the guideline is enabled

        tags : typing.Optional[GuidelineTagsUpdateParams]

        metadata : typing.Optional[GuidelineMetadataUpdateParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidelineWithRelationshipsAndToolAssociations
            Guideline successfully updated. Returns the updated guideline with its relationships and tool associations.

        Examples
        --------
        import asyncio

        from parlant.client import (
            AsyncParlantClient,
            GuidelineMetadataUpdateParams,
            GuidelineRelationshipAddition,
            GuidelineRelationshipUpdateParams,
            GuidelineToolAssociationUpdateParams,
            ToolId,
        )

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.guidelines.update(
                guideline_id="IUCGT-l4pS",
                condition="when the customer asks about pricing",
                action="provide current pricing information",
                relationships=GuidelineRelationshipUpdateParams(
                    add=[
                        GuidelineRelationshipAddition(
                            kind="entailment",
                        )
                    ],
                    remove=["guideline_relationship_id_789yz"],
                ),
                tool_associations=GuidelineToolAssociationUpdateParams(
                    add=[
                        ToolId(
                            service_name="new_service",
                            tool_name="new_tool",
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
                metadata=GuidelineMetadataUpdateParams(
                    add={"key1": "value1", "key2": "value2"},
                    remove=["key3", "key4"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guidelines/{jsonable_encoder(guideline_id)}",
            method="PATCH",
            json={
                "condition": condition,
                "action": action,
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships,
                    annotation=GuidelineRelationshipUpdateParams,
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
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata,
                    annotation=GuidelineMetadataUpdateParams,
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GuidelineWithRelationshipsAndToolAssociations,
                    parse_obj_as(
                        type_=GuidelineWithRelationshipsAndToolAssociations,  # type: ignore
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
