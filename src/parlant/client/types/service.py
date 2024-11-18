# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .tool_service_kind_dto import ToolServiceKindDto
import typing
from .tool import Tool
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Service(UniversalBaseModel):
    name: str
    kind: ToolServiceKindDto
    url: str
    tools: typing.Optional[typing.List[Tool]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow