# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tag import Tag
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tag]:
        """
        List all tags.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            List of all the `Tag`s.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tags.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "tags/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Tag],
                    parse_obj_as(
                        type_=typing.List[Tag],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Creates a new `Tag` with the provided `name`.

        Parameters
        ----------
        name : str
            Name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag successfully generated. Returns a `Tag` object with a unique generated id.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tags.create(
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "tags/",
            method="POST",
            json={
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,  # type: ignore
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
        self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Retrieves the `Tag` with the provided `id`.

        Parameters
        ----------
        tag_id : str
            Unique identifier for the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag successfully retrieved.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tags.retrieve(
            tag_id="tag_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tags/{jsonable_encoder(tag_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,  # type: ignore
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
        self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tag_id : str

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
        client.tags.delete(
            tag_id="tag_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tags/{jsonable_encoder(tag_id)}",
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
        tag_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an existing `Tag`'s fields (namely: `name`).

        Parameters
        ----------
        tag_id : str
            Unique identifier for the tag

        name : str
            Name of the tag

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
        client.tags.update(
            tag_id="tag_id",
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tags/{jsonable_encoder(tag_id)}",
            method="PATCH",
            json={
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
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


class AsyncTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tag]:
        """
        List all tags.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            List of all the `Tag`s.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tags.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tags/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Tag],
                    parse_obj_as(
                        type_=typing.List[Tag],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Creates a new `Tag` with the provided `name`.

        Parameters
        ----------
        name : str
            Name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag successfully generated. Returns a `Tag` object with a unique generated id.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tags.create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tags/",
            method="POST",
            json={
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,  # type: ignore
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
        self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Retrieves the `Tag` with the provided `id`.

        Parameters
        ----------
        tag_id : str
            Unique identifier for the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag successfully retrieved.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tags.retrieve(
                tag_id="tag_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tags/{jsonable_encoder(tag_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,  # type: ignore
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
        self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tag_id : str

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
            await client.tags.delete(
                tag_id="tag_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tags/{jsonable_encoder(tag_id)}",
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
        tag_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an existing `Tag`'s fields (namely: `name`).

        Parameters
        ----------
        tag_id : str
            Unique identifier for the tag

        name : str
            Name of the tag

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
            await client.tags.update(
                tag_id="tag_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tags/{jsonable_encoder(tag_id)}",
            method="PATCH",
            json={
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
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
