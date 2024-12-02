# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .guideline import Guideline
import typing
from .guideline_connection import GuidelineConnection
import pydantic
from .guideline_tool_association import GuidelineToolAssociation
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GuidelineWithConnectionsAndToolAssociations(UniversalBaseModel):
    """
    A Guideline with its connections and tool associations.
    """

    guideline: Guideline
    connections: typing.List[GuidelineConnection] = pydantic.Field()
    """
    A collection of the `Guideline`'s connections
    """

    tool_associations: typing.List[GuidelineToolAssociation] = pydantic.Field()
    """
    A collection of the `Guideline`'s tool associations
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
