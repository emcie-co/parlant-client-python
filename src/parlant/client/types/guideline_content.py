# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GuidelineContent(UniversalBaseModel):
    """
    A container for the values of a Guideline's content
    """

    condition: str = pydantic.Field()
    """
    If this condition is satisfied, the action will be performed
    """

    action: str = pydantic.Field()
    """
    This action will be performed if the condition is satisfied
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
