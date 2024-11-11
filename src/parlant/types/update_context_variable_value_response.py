# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .context_variable_value import ContextVariableValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class UpdateContextVariableValueResponse(UniversalBaseModel):
    context_variable_value: ContextVariableValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
