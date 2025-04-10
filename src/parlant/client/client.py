# This file was auto-generated by Fern from our API Definition.

import typing
import httpx
from .core.client_wrapper import SyncClientWrapper
from .agents.client import AgentsClient
from .guidelines.client import GuidelinesClient
from .glossary.client import GlossaryClient
from .context_variables.client import ContextVariablesClient
from .sessions.client import SessionsClient
from .evaluations.client import EvaluationsClient
from .services.client import ServicesClient
from .tags.client import TagsClient
from .customers.client import CustomersClient
from .core.client_wrapper import AsyncClientWrapper
from .agents.client import AsyncAgentsClient
from .guidelines.client import AsyncGuidelinesClient
from .glossary.client import AsyncGlossaryClient
from .context_variables.client import AsyncContextVariablesClient
from .sessions.client import AsyncSessionsClient
from .evaluations.client import AsyncEvaluationsClient
from .services.client import AsyncServicesClient
from .tags.client import AsyncTagsClient
from .customers.client import AsyncCustomersClient


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
        self.guidelines = GuidelinesClient(client_wrapper=self._client_wrapper)
        self.glossary = GlossaryClient(client_wrapper=self._client_wrapper)
        self.context_variables = ContextVariablesClient(
            client_wrapper=self._client_wrapper
        )
        self.sessions = SessionsClient(client_wrapper=self._client_wrapper)
        self.evaluations = EvaluationsClient(client_wrapper=self._client_wrapper)
        self.services = ServicesClient(client_wrapper=self._client_wrapper)
        self.tags = TagsClient(client_wrapper=self._client_wrapper)
        self.customers = CustomersClient(client_wrapper=self._client_wrapper)


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
        self.guidelines = AsyncGuidelinesClient(client_wrapper=self._client_wrapper)
        self.glossary = AsyncGlossaryClient(client_wrapper=self._client_wrapper)
        self.context_variables = AsyncContextVariablesClient(
            client_wrapper=self._client_wrapper
        )
        self.sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        self.evaluations = AsyncEvaluationsClient(client_wrapper=self._client_wrapper)
        self.services = AsyncServicesClient(client_wrapper=self._client_wrapper)
        self.tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        self.customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
