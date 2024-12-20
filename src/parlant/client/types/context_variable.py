# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .tool_id import ToolId
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ContextVariable(UniversalBaseModel):
    """
    Represents a type of customer or tag data that the agent tracks.

    Context variables store information that helps the agent provide
    personalized responses based on each customer's or group's specific situation,
    such as their subscription tier, usage patterns, or preferences.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the context variable
    """

    name: str = pydantic.Field()
    """
    Name of the context variable
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the context variable's purpose
    """

    tool_id: typing.Optional[ToolId] = None
    freshness_rules: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cron expression defining the freshness rules
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
