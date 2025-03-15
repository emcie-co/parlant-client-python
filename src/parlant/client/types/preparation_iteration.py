# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .preparation_iteration_generations import PreparationIterationGenerations
import typing
from .guideline_match_item import GuidelineMatchItem
import pydantic
from .tool_call import ToolCall
from .preparation_iteration_term import PreparationIterationTerm
from .context_variable_and_value import ContextVariableAndValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PreparationIteration(UniversalBaseModel):
    """
    Information about a preparation iteration.
    """

    generations: PreparationIterationGenerations
    guideline_match_items: typing.List[GuidelineMatchItem] = pydantic.Field()
    """
    List of guideline match items used in preparation for this iteration
    """

    tool_calls: typing.List[ToolCall] = pydantic.Field()
    """
    List of tool calls made in preparation for this iteration
    """

    terms: typing.List[PreparationIterationTerm] = pydantic.Field()
    """
    List of terms participating in the preparation for this iteration
    """

    context_variables: typing.List[ContextVariableAndValue] = pydantic.Field()
    """
    List of context variables (and their values) that participated in the preparation for this iteration
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
