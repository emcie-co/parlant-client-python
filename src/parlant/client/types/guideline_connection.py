# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .guideline import Guideline
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GuidelineConnection(UniversalBaseModel):
    """
    Represents a connection between two guidelines.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the `GuildelineConnection`
    """

    source: Guideline
    target: Guideline
    indirect: bool = pydantic.Field()
    """
    `True` if there is a path from `source` to `target` but no direct connection
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
