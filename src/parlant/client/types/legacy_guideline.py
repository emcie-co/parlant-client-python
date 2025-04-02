# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LegacyGuideline(UniversalBaseModel):
    """
    Assigns an id to the condition-action pair
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the guideline
    """

    condition: str = pydantic.Field()
    """
    If this condition is satisfied, the action will be performed
    """

    action: str = pydantic.Field()
    """
    This action will be performed if the condition is satisfied
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the guideline is enabled
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
