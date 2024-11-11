# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .guideline_payload import GuidelinePayload
from .guideline_invoice_data import GuidelineInvoiceData
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GuidelineInvoice(UniversalBaseModel):
    payload: GuidelinePayload
    checksum: str
    approved: bool
    data: GuidelineInvoiceData
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
