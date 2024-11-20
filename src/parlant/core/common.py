from __future__ import annotations

from typing import Any, Mapping, NewType, Optional, Sequence, TypeAlias, Union

import nanoid  # type: ignore
import semver  # type: ignore
from pydantic import BaseModel, ConfigDict


def _without_dto_suffix(obj: Any, *args: Any) -> str:
    if isinstance(obj, str):
        name = obj
        if name.endswith("DTO"):
            return name[:-3]
        return name
    if isinstance(obj, type):
        name = obj.__name__
        if name.endswith("DTO"):
            return name[:-3]
        return name
    else:
        raise Exception("Invalid input to _without_dto_suffix()")


class DefaultBaseModel(BaseModel):
    """
    Base class for all Parlant Pydantic models.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_default=True,
        model_title_generator=_without_dto_suffix,
    )


JSONSerializable: TypeAlias = Union[
    str,
    int,
    float,
    bool,
    None,
    Mapping[str, "JSONSerializable"],
    Sequence["JSONSerializable"],
    Optional[str],
    Optional[int],
    Optional[float],
    Optional[bool],
    Optional[None],
    Optional[Mapping[str, "JSONSerializable"]],
    Optional[Sequence["JSONSerializable"]],
]

UniqueId = NewType("UniqueId", str)
AgentId = NewType("AgentId", str)
ContextVariableId = NewType("ContextVariableId", str)
EndUserId = NewType("EndUserId", str)
GuidelineId = NewType("GuidelineId", str)


class Version:
    String = NewType("String", str)

    @staticmethod
    def from_string(version_string: Version.String | str) -> Version:
        result = Version(major=0, minor=0, patch=0)
        result._v = semver.Version.parse(version_string)
        return result

    def __init__(
        self,
        major: int,
        minor: int,
        patch: int,
        prerelease: Optional[str] = None,
    ) -> None:
        self._v = semver.Version(
            major=major,
            minor=minor,
            patch=patch,
            prerelease=prerelease,
        )

    def to_string(self) -> Version.String:
        return Version.String(str(self._v))


class ItemNotFoundError(Exception):
    def __init__(self, item_id: UniqueId, message: Optional[str] = None) -> None:
        super().__init__(f"Item '{item_id}' not found" + (f": {message}" if message else ""))


def generate_id() -> UniqueId:
    return UniqueId(nanoid.generate(size=10))
