# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GuidelineMetadataUpdateParams(UniversalBaseModel):
    """
    Parameters for updating the metadata of a guideline.
    """

    add: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = (
        pydantic.Field(default=None)
    )
    """
    Metadata for the guideline
    """

    remove: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Metadata keys to remove from the guideline
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
