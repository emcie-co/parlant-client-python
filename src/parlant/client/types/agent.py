# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Agent(UniversalBaseModel):
    """
    An agent is a specialized AI personality crafted for a specific service role.

    Agents form the basic unit of conversational customization: all behavioral configurations
    are made at the agent level.

    Use this model for representing complete agent information in API responses.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the agent
    """

    name: str = pydantic.Field()
    """
    The display name of the agent, mainly for management purposes
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Detailed description of the agent's purpose and capabilities
    """

    creation_utc: dt.datetime = pydantic.Field()
    """
    UTC timestamp of when the agent was created
    """

    max_engine_iterations: int = pydantic.Field()
    """
    Maximum number of processing iterations the agent can perform per request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
