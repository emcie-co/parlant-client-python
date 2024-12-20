# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import datetime as dt
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Customer(UniversalBaseModel):
    """
    Represents a customer in the system.

    Customers are entities that interact with agents through sessions. Each customer
    can have metadata stored in the extra field and can be tagged for categorization.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the customer
    """

    creation_utc: dt.datetime = pydantic.Field()
    """
    UTC timestamp of when the agent was created
    """

    name: str = pydantic.Field()
    """
    An arbitrary string that indentifies and/or describes the customer
    """

    extra: typing.Dict[str, str] = pydantic.Field()
    """
    Key-value pairs (`str: str`) to describe the customer
    """

    tags: typing.List[str] = pydantic.Field()
    """
    Collection of ids of tags that describe the customer
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
