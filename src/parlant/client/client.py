# This file was auto-generated by Fern from our API Definition.

import typing
import httpx
from .core.client_wrapper import SyncClientWrapper
from .agents.client import AgentsClient
from .sessions.client import SessionsClient
from .evaluations.client import EvaluationsClient
from .services.client import ServicesClient
from .tags.client import TagsClient
from .glossary.client import GlossaryClient
from .customers.client import CustomersClient
from .fragments.client import FragmentsClient
from .context_variables.client import ContextVariablesClient
from .guidelines.client import GuidelinesClient
from .core.request_options import RequestOptions
from .types.context_variable import ContextVariable
from .core.pydantic_utilities import parse_obj_as
from .errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from .core.api_error import ApiError
from .core.jsonable_encoder import jsonable_encoder
from .core.client_wrapper import AsyncClientWrapper
from .agents.client import AsyncAgentsClient
from .sessions.client import AsyncSessionsClient
from .evaluations.client import AsyncEvaluationsClient
from .services.client import AsyncServicesClient
from .tags.client import AsyncTagsClient
from .glossary.client import AsyncGlossaryClient
from .customers.client import AsyncCustomersClient
from .fragments.client import AsyncFragmentsClient
from .context_variables.client import AsyncContextVariablesClient
from .guidelines.client import AsyncGuidelinesClient


class ParlantClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from parlant.client import ParlantClient

    client = ParlantClient(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else None
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(
                timeout=_defaulted_timeout, follow_redirects=follow_redirects
            )
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.agents = AgentsClient(client_wrapper=self._client_wrapper)
        self.sessions = SessionsClient(client_wrapper=self._client_wrapper)
        self.evaluations = EvaluationsClient(client_wrapper=self._client_wrapper)
        self.services = ServicesClient(client_wrapper=self._client_wrapper)
        self.tags = TagsClient(client_wrapper=self._client_wrapper)
        self.glossary = GlossaryClient(client_wrapper=self._client_wrapper)
        self.customers = CustomersClient(client_wrapper=self._client_wrapper)
        self.fragments = FragmentsClient(client_wrapper=self._client_wrapper)
        self.context_variables = ContextVariablesClient(
            client_wrapper=self._client_wrapper
        )
        self.guidelines = GuidelinesClient(client_wrapper=self._client_wrapper)

    def list_variables(
        self,
        *,
        tag_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ContextVariable]:
        """
        Lists all context variables set for the provided tag or all context variables if no tag is provided

        Parameters
        ----------
        tag_id : typing.Optional[str]
            The tag ID to filter context variables by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContextVariable]
            Successful Response

        Examples
        --------
        from parlant.client import ParlantClient

        client = ParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_variables()
        """
        _response = self._client_wrapper.httpx_client.request(
            "context-variables",
            method="GET",
            params={
                "tag_id": tag_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ContextVariable],
                    parse_obj_as(
                        type_=typing.List[ContextVariable],  # type: ignore
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

    def delete_variable(
        self,
        variable_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a context variable

        Parameters
        ----------
        variable_id : str
            Unique identifier for the context variable

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
        client.delete_variable(
            variable_id="v9a8r7i6b5",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context-variables/{jsonable_encoder(variable_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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


class AsyncParlantClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from parlant.client import AsyncParlantClient

    client = AsyncParlantClient(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else None
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(
                timeout=_defaulted_timeout, follow_redirects=follow_redirects
            )
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        self.sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        self.evaluations = AsyncEvaluationsClient(client_wrapper=self._client_wrapper)
        self.services = AsyncServicesClient(client_wrapper=self._client_wrapper)
        self.tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        self.glossary = AsyncGlossaryClient(client_wrapper=self._client_wrapper)
        self.customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        self.fragments = AsyncFragmentsClient(client_wrapper=self._client_wrapper)
        self.context_variables = AsyncContextVariablesClient(
            client_wrapper=self._client_wrapper
        )
        self.guidelines = AsyncGuidelinesClient(client_wrapper=self._client_wrapper)

    async def list_variables(
        self,
        *,
        tag_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ContextVariable]:
        """
        Lists all context variables set for the provided tag or all context variables if no tag is provided

        Parameters
        ----------
        tag_id : typing.Optional[str]
            The tag ID to filter context variables by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContextVariable]
            Successful Response

        Examples
        --------
        import asyncio

        from parlant.client import AsyncParlantClient

        client = AsyncParlantClient(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_variables()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "context-variables",
            method="GET",
            params={
                "tag_id": tag_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ContextVariable],
                    parse_obj_as(
                        type_=typing.List[ContextVariable],  # type: ignore
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

    async def delete_variable(
        self,
        variable_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a context variable

        Parameters
        ----------
        variable_id : str
            Unique identifier for the context variable

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
            await client.delete_variable(
                variable_id="v9a8r7i6b5",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context-variables/{jsonable_encoder(variable_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
