# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.term import Term
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GlossaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_terms(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Term]:
        """
        Retrieves a list of all terms in the agent's glossary.

        Returns an empty list if no terms associated to the provided agent's ID.
        Terms are returned in no guaranteed order.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Term]
            List of all terms in the agent's glossary.

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.glossary.list_terms(
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Term],
                    parse_obj_as(
                        type_=typing.List[Term],  # type: ignore
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

    def create_term(
        self,
        agent_id: str,
        *,
        name: str,
        description: str,
        synonyms: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Term:
        """
        Creates a new term in the agent's glossary.

        The term will be initialized with the provided name and description, and optional synonyms.
        The term will be associated with the specified agent.
        A unique identifier will be automatically generated.

        Default behaviors:

        - `synonyms` defaults to an empty list if not provided

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        name : str
            The name of the term, e.g., 'Gas' in blockchain.

        description : str
            A detailed description of the term

        synonyms : typing.Optional[typing.Sequence[str]]
            A list of synonyms for the term, including alternate contexts if applicable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Term
            Term successfully created. Returns the complete term object including generated ID

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.glossary.create_term(
            agent_id="agent_id",
            name="Gas",
            description="A unit in Ethereum that measures the computational effort to execute transactions or smart contracts",
            synonyms=["Transaction Fee", "Blockchain Fuel"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms",
            method="POST",
            json={
                "name": name,
                "description": description,
                "synonyms": synonyms,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Term,
                    parse_obj_as(
                        type_=Term,  # type: ignore
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

    def retrieve_term(
        self,
        agent_id: str,
        term_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Term:
        """
        Retrieves details of a specific term by ID for a given agent.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        term_id : str
            Unique identifier for the term

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Term
            Term details successfully retrieved. Returns the complete term object

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.glossary.retrieve_term(
            agent_id="agent_id",
            term_id="term_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms/{jsonable_encoder(term_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Term,
                    parse_obj_as(
                        type_=Term,  # type: ignore
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

    def delete_term(
        self,
        agent_id: str,
        term_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a term from the agent.

        Deleting a non-existent term will return 404.
        No content will be returned from a successful deletion.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        term_id : str
            Unique identifier for the term

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
        client.glossary.delete_term(
            agent_id="agent_id",
            term_id="term_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms/{jsonable_encoder(term_id)}",
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

    def update_term(
        self,
        agent_id: str,
        term_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        synonyms: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Term:
        """
        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        term_id : str
            Unique identifier for the term

        name : typing.Optional[str]
            The name of the term, e.g., 'Gas' in blockchain.

        description : typing.Optional[str]
            A detailed description of the term

        synonyms : typing.Optional[typing.Sequence[str]]
            A list of synonyms for the term, including alternate contexts if applicable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Term
            Term successfully updated. Returns the updated term object

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.glossary.update_term(
            agent_id="agent_id",
            term_id="term_id",
            name="Gas",
            description="A unit in Ethereum that measures the computational effort to execute transactions or smart contracts",
            synonyms=["Transaction Fee", "Blockchain Fuel"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms/{jsonable_encoder(term_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "synonyms": synonyms,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Term,
                    parse_obj_as(
                        type_=Term,  # type: ignore
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


class AsyncGlossaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_terms(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Term]:
        """
        Retrieves a list of all terms in the agent's glossary.

        Returns an empty list if no terms associated to the provided agent's ID.
        Terms are returned in no guaranteed order.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Term]
            List of all terms in the agent's glossary.

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.glossary.list_terms(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Term],
                    parse_obj_as(
                        type_=typing.List[Term],  # type: ignore
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

    async def create_term(
        self,
        agent_id: str,
        *,
        name: str,
        description: str,
        synonyms: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Term:
        """
        Creates a new term in the agent's glossary.

        The term will be initialized with the provided name and description, and optional synonyms.
        The term will be associated with the specified agent.
        A unique identifier will be automatically generated.

        Default behaviors:

        - `synonyms` defaults to an empty list if not provided

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        name : str
            The name of the term, e.g., 'Gas' in blockchain.

        description : str
            A detailed description of the term

        synonyms : typing.Optional[typing.Sequence[str]]
            A list of synonyms for the term, including alternate contexts if applicable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Term
            Term successfully created. Returns the complete term object including generated ID

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.glossary.create_term(
                agent_id="agent_id",
                name="Gas",
                description="A unit in Ethereum that measures the computational effort to execute transactions or smart contracts",
                synonyms=["Transaction Fee", "Blockchain Fuel"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms",
            method="POST",
            json={
                "name": name,
                "description": description,
                "synonyms": synonyms,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Term,
                    parse_obj_as(
                        type_=Term,  # type: ignore
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

    async def retrieve_term(
        self,
        agent_id: str,
        term_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Term:
        """
        Retrieves details of a specific term by ID for a given agent.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        term_id : str
            Unique identifier for the term

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Term
            Term details successfully retrieved. Returns the complete term object

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.glossary.retrieve_term(
                agent_id="agent_id",
                term_id="term_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms/{jsonable_encoder(term_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Term,
                    parse_obj_as(
                        type_=Term,  # type: ignore
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

    async def delete_term(
        self,
        agent_id: str,
        term_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a term from the agent.

        Deleting a non-existent term will return 404.
        No content will be returned from a successful deletion.

        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        term_id : str
            Unique identifier for the term

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
            await client.glossary.delete_term(
                agent_id="agent_id",
                term_id="term_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms/{jsonable_encoder(term_id)}",
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

    async def update_term(
        self,
        agent_id: str,
        term_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        synonyms: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Term:
        """
        Parameters
        ----------
        agent_id : str
            Unique identifier for the agent associated with the term.

        term_id : str
            Unique identifier for the term

        name : typing.Optional[str]
            The name of the term, e.g., 'Gas' in blockchain.

        description : typing.Optional[str]
            A detailed description of the term

        synonyms : typing.Optional[typing.Sequence[str]]
            A list of synonyms for the term, including alternate contexts if applicable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Term
            Term successfully updated. Returns the updated term object

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.glossary.update_term(
                agent_id="agent_id",
                term_id="term_id",
                name="Gas",
                description="A unit in Ethereum that measures the computational effort to execute transactions or smart contracts",
                synonyms=["Transaction Fee", "Blockchain Fuel"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{jsonable_encoder(agent_id)}/terms/{jsonable_encoder(term_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "synonyms": synonyms,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Term,
                    parse_obj_as(
                        type_=Term,  # type: ignore
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
