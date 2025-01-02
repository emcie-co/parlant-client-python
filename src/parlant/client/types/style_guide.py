# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .style_guide_content import StyleGuideContent
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class StyleGuide(UniversalBaseModel):
    """
    Assigns an id to the style-guide content
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the style guide
    """

    content: StyleGuideContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow