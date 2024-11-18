# This file was auto-generated by Fern from our API Definition.

import typing
from .context_variable_value_dto_data_item import ContextVariableValueDtoDataItem
from .context_variable_value_dto_data_five_value import (
    ContextVariableValueDtoDataFiveValue,
)

Data = typing.Union[
    str,
    int,
    float,
    bool,
    typing.List[ContextVariableValueDtoDataItem],
    typing.Dict[str, ContextVariableValueDtoDataFiveValue],
]