# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .day_of_week_dto import DayOfWeekDto
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FreshnessRules(UniversalBaseModel):
    """
    Rules for validating data freshness.
    """

    months: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of valid months (1-12)
    """

    days_of_month: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of valid days of month (1-31)
    """

    days_of_week: typing.Optional[typing.List[DayOfWeekDto]] = pydantic.Field(
        default=None
    )
    """
    List of valid days of week
    """

    hours: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of valid hours (0-23)
    """

    minutes: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of valid minutes (0-59)
    """

    seconds: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of valid seconds (0-59)
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
