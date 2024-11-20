from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import (
    Literal,
    Mapping,
    NewType,
    NotRequired,
    Optional,
    TypeAlias,
    TypedDict,
)

from parlant.core.common import (
    AgentId,
    ContextVariableId,
    EndUserId,
    GuidelineId,
    JSONSerializable,
)

SessionId = NewType("SessionId", str)

EventId = NewType("EventId", str)
EventSource: TypeAlias = Literal[
    "end_user",
    "end_user_ui",
    "human_agent",
    "human_agent_on_behalf_of_ai_agent",
    "ai_agent",
]
EventKind: TypeAlias = Literal["message", "tool", "status", "custom"]


@dataclass(frozen=True)
class Event:
    id: EventId
    source: EventSource
    kind: EventKind
    creation_utc: datetime
    offset: int
    correlation_id: str
    data: JSONSerializable
    deleted: bool

    def is_from_client(self) -> bool:
        return self.source in list[EventSource](
            [
                "end_user",
                "end_user_ui",
            ]
        )

    def is_from_server(self) -> bool:
        return self.source in list[EventSource](
            [
                "human_agent",
                "human_agent_on_behalf_of_ai_agent",
                "ai_agent",
            ]
        )


class Participant(TypedDict):
    id: NotRequired[AgentId | EndUserId | None]
    display_name: str


class MessageEventData(TypedDict):
    message: str
    participant: Participant
    flagged: NotRequired[bool]
    tags: NotRequired[list[str]]


SessionMode: TypeAlias = Literal["auto", "manual"]


class ControlOptions(TypedDict, total=False):
    mode: SessionMode


class ToolResult(TypedDict):
    data: JSONSerializable
    metadata: Mapping[str, JSONSerializable]
    control: ControlOptions


class ToolCall(TypedDict):
    tool_id: str
    arguments: Mapping[str, JSONSerializable]
    result: ToolResult


class ToolEventData(TypedDict):
    tool_calls: list[ToolCall]


SessionStatus: TypeAlias = Literal[
    "acknowledged",
    "cancelled",
    "processing",
    "ready",
    "typing",
    "error",
]


class StatusEventData(TypedDict):
    acknowledged_offset: NotRequired[int]
    status: SessionStatus
    data: JSONSerializable


class GuidelineProposition(TypedDict):
    guideline_id: GuidelineId
    condition: str
    action: str
    score: int
    rationale: str


class ContextVariable(TypedDict):
    id: ContextVariableId
    name: str
    description: Optional[str]
    key: str
    value: JSONSerializable
