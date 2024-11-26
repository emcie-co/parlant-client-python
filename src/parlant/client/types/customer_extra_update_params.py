# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CustomerExtraUpdateParams(UniversalBaseModel):
    """
    Parameters for updating a customer's extra metadata.

    Optional:
    add: Dictionary of new or updated key-value pairs
    remove: List of keys to remove from extra metadata
    """

    add: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    remove: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
