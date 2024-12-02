# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customer import Customer
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..types.customer_extra_update_params import CustomerExtraUpdateParams
from ..types.tags_update_params import TagsUpdateParams
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CustomersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Customer]:
        """
        Retrieves a list of all customers in the system.

        Returns an empty list if no customers exist.
        Customers are returned in no guaranteed order.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Customer]
            List of all customers in the system.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.customers.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "customers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Customer],
                    parse_obj_as(
                        type_=typing.List[Customer],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        name: str,
        extra: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Creates a new `Customer` in the system.

        A `Customer` may be created with as little as a `name`.
        `extra` key-value pairs and additional `tags` may be attached to a `Customer`.

        Parameters
        ----------
        name : str
            An arbitrary string that indentifies and/or describes the `Customer`

        extra : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Key-value pairs (`str: str`) to describe the customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Customer successfully created. Returns the new `Customer` object.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.customers.create(
            name="Scooby",
            extra={"VIP": "Yes", "email": "scooby@dooby.do"},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "customers/",
            method="POST",
            json={
                "name": name,
                "extra": extra,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Customer,
                    parse_obj_as(
                        type_=Customer,  # type: ignore
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
        customer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Retrieves details of a specific customer by ID.

        Returns a complete customer object including their metadata and tags.
        The customer must exist in the system.

        Parameters
        ----------
        customer_id : str
            Unique identifier for the customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Customer details successfully retrieved. Returns the Customer object.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.customers.retrieve(
            customer_id="customer_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{jsonable_encoder(customer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Customer,
                    parse_obj_as(
                        type_=Customer,  # type: ignore
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
        customer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a customer from the system.

        Deleting a non-existent customer will return 404.
        No content will be returned from a successful deletion.

        Parameters
        ----------
        customer_id : str

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
        client.customers.delete(
            customer_id="customer_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{jsonable_encoder(customer_id)}",
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
        customer_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        extra: typing.Optional[CustomerExtraUpdateParams] = OMIT,
        tags: typing.Optional[TagsUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Updates an existing customer's attributes.

        Only provided attributes will be updated; others remain unchanged.
        The customer's ID and creation timestamp cannot be modified.
        Extra metadata and tags can be added or removed independently.

        Parameters
        ----------
        customer_id : str
            Unique identifier for the customer

        name : typing.Optional[str]
            Optionally, an arbitrary string that indentifies and/or describes the `Customer`

        extra : typing.Optional[CustomerExtraUpdateParams]
            Optional changes to the `Customer`'s extra metadata

        tags : typing.Optional[TagsUpdateParams]
            Optional changes to the `Customer`'s tags metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Customer successfully updated. Returns the updated Customer object.

        Examples
        --------
        from parlant.client import CustomerExtraUpdateParams, ParlantClient, TagsUpdateParams

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.customers.update(
            customer_id="customer_id",
            name="Scooby",
            extra=CustomerExtraUpdateParams(
                add={"VIP": "Yes", "email": "scooby@dooby.do"},
                remove=["old_email", "old_title"],
            ),
            tags=TagsUpdateParams(
                add=["VIP", "New User"],
                remove=["old_email", "old_title"],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{jsonable_encoder(customer_id)}",
            method="PATCH",
            json={
                "name": name,
                "extra": convert_and_respect_annotation_metadata(
                    object_=extra,
                    annotation=CustomerExtraUpdateParams,
                    direction="write",
                ),
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=TagsUpdateParams, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Customer,
                    parse_obj_as(
                        type_=Customer,  # type: ignore
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


class AsyncCustomersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Customer]:
        """
        Retrieves a list of all customers in the system.

        Returns an empty list if no customers exist.
        Customers are returned in no guaranteed order.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Customer]
            List of all customers in the system.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.customers.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Customer],
                    parse_obj_as(
                        type_=typing.List[Customer],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        name: str,
        extra: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Creates a new `Customer` in the system.

        A `Customer` may be created with as little as a `name`.
        `extra` key-value pairs and additional `tags` may be attached to a `Customer`.

        Parameters
        ----------
        name : str
            An arbitrary string that indentifies and/or describes the `Customer`

        extra : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Key-value pairs (`str: str`) to describe the customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Customer successfully created. Returns the new `Customer` object.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.customers.create(
                name="Scooby",
                extra={"VIP": "Yes", "email": "scooby@dooby.do"},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customers/",
            method="POST",
            json={
                "name": name,
                "extra": extra,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Customer,
                    parse_obj_as(
                        type_=Customer,  # type: ignore
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
        customer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Retrieves details of a specific customer by ID.

        Returns a complete customer object including their metadata and tags.
        The customer must exist in the system.

        Parameters
        ----------
        customer_id : str
            Unique identifier for the customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Customer details successfully retrieved. Returns the Customer object.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.customers.retrieve(
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{jsonable_encoder(customer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Customer,
                    parse_obj_as(
                        type_=Customer,  # type: ignore
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
        customer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a customer from the system.

        Deleting a non-existent customer will return 404.
        No content will be returned from a successful deletion.

        Parameters
        ----------
        customer_id : str

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
            await client.customers.delete(
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{jsonable_encoder(customer_id)}",
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
        customer_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        extra: typing.Optional[CustomerExtraUpdateParams] = OMIT,
        tags: typing.Optional[TagsUpdateParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Updates an existing customer's attributes.

        Only provided attributes will be updated; others remain unchanged.
        The customer's ID and creation timestamp cannot be modified.
        Extra metadata and tags can be added or removed independently.

        Parameters
        ----------
        customer_id : str
            Unique identifier for the customer

        name : typing.Optional[str]
            Optionally, an arbitrary string that indentifies and/or describes the `Customer`

        extra : typing.Optional[CustomerExtraUpdateParams]
            Optional changes to the `Customer`'s extra metadata

        tags : typing.Optional[TagsUpdateParams]
            Optional changes to the `Customer`'s tags metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Customer successfully updated. Returns the updated Customer object.

        Examples
        --------
        import asyncio

        from parlant.client import (
            AsyncParlantClient,
            CustomerExtraUpdateParams,
            TagsUpdateParams,
        )

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.customers.update(
                customer_id="customer_id",
                name="Scooby",
                extra=CustomerExtraUpdateParams(
                    add={"VIP": "Yes", "email": "scooby@dooby.do"},
                    remove=["old_email", "old_title"],
                ),
                tags=TagsUpdateParams(
                    add=["VIP", "New User"],
                    remove=["old_email", "old_title"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{jsonable_encoder(customer_id)}",
            method="PATCH",
            json={
                "name": name,
                "extra": convert_and_respect_annotation_metadata(
                    object_=extra,
                    annotation=CustomerExtraUpdateParams,
                    direction="write",
                ),
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=TagsUpdateParams, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Customer,
                    parse_obj_as(
                        type_=Customer,  # type: ignore
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
