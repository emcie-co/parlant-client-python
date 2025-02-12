# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import datetime as dt
import typing
from .fragment_field import FragmentField
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Fragment(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the tag
    """

    creation_utc: dt.datetime = pydantic.Field()
    """
    UTC timestamp of when the fragment was created
    """

    value: str = pydantic.Field()
    """
    The textual content of the fragment.
    """

    fields: typing.List[FragmentField] = pydantic.Field()
    """
    A sequence of fragment fields associated with the fragment.
    """

    tags: typing.List[str] = pydantic.Field()
    """
    Collection of tag IDs associated with the fragment.
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
