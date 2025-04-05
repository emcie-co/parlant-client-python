# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .guideline import Guideline
from .guideline_relationship_tag import GuidelineRelationshipTag
from .guideline_relationship_kind_dto import GuidelineRelationshipKindDto
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GuidelineRelationship(UniversalBaseModel):
    """
    Represents a guideline relationship addition.

    Only one of `source_guideline` and `source_tag` can have a value.
    Only one of `target_guideline` and `target_tag` can have a value.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the guideline relationship
    """

    source_guideline: typing.Optional[Guideline] = None
    source_tag: typing.Optional[GuidelineRelationshipTag] = None
    target_guideline: typing.Optional[Guideline] = None
    target_tag: typing.Optional[GuidelineRelationshipTag] = None
    indirect: bool = pydantic.Field()
    """
    `True` if there is a path from `source` to `target` but no direct relationship
    """

    kind: GuidelineRelationshipKindDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
