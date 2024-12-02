# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .context_variable import ContextVariable
import typing
from .context_variable_value import ContextVariableValue
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ContextVariableReadResult(UniversalBaseModel):
    """
    Complete context variable data including its values.
    """

    context_variable: ContextVariable
    key_value_pairs: typing.Optional[
        typing.Dict[str, typing.Optional[ContextVariableValue]]
    ] = pydantic.Field(default=None)
    """
    Collection of key-value pairs associated with the variable
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
