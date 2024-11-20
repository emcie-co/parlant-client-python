from __future__ import annotations

import asyncio
import enum
import inspect
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from types import TracebackType
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Literal,
    NamedTuple,
    NewType,
    Optional,
    Sequence,
    TypeAlias,
    TypedDict,
    Union,
    Unpack,
    get_args,
    overload,
)

import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from parlant.core.common import DefaultBaseModel, JSONSerializable
from parlant.core.tools import (
    EnumValueType,
    Tool,
    ToolContext,
    ToolParameter,
    ToolParameterType,
    ToolResult,
)

SessionId = NewType("SessionId", str)
SessionStatus: TypeAlias = Literal[
    "acknowledged",
    "cancelled",
    "processing",
    "ready",
    "typing",
    "error",
]

ToolFunction = Union[
    Callable[
        [ToolContext],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any, Any],
        Union[Awaitable[ToolResult], ToolResult],
    ],
    Callable[
        [ToolContext, Any, Any, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any, Any, Any, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any, Any, Any, Any, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any, Any, Any, Any, Any, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any, Any, Any, Any, Any, Any, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
    Callable[
        [ToolContext, Any, Any, Any, Any, Any, Any, Any, Any],
        Union[ToolResult, Awaitable[ToolResult]],
    ],
]


@dataclass(frozen=True)
class ToolEntry:
    tool: Tool
    function: ToolFunction

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.function(*args, **kwargs)


class _ToolDecoratorParams(TypedDict, total=False):
    id: str
    name: str
    consequential: bool


_ToolParameterType = Union[str, int, float, bool]


class _ResolvedToolParameterTyped(NamedTuple):
    t: type[_ToolParameterType]
    is_optional: bool


def _tool_decorator_impl(
    **kwargs: Unpack[_ToolDecoratorParams],
) -> Callable[[ToolFunction], ToolEntry]:
    def _resolve_param_type(param: inspect.Parameter) -> _ResolvedToolParameterTyped:
        if not param.annotation.__name__ == "Optional":
            return _ResolvedToolParameterTyped(
                t=param.annotation,
                is_optional=False,
            )
        else:
            return _ResolvedToolParameterTyped(
                t=get_args(param.annotation)[0],
                is_optional=True,
            )

    def _ensure_valid_tool_signature(func: ToolFunction) -> None:
        signature = inspect.signature(func)

        parameters = list(signature.parameters.values())

        assert (
            len(parameters) >= 1
        ), "A tool function must accept a parameter 'context: ToolContext'"

        assert (
            parameters[0].name == "context"
        ), "A tool function's first parameter must be 'context: ToolContext'"
        assert (
            parameters[0].annotation == ToolContext
        ), "A tool function's first parameter must be 'context: ToolContext'"

        assert (
            signature.return_annotation == ToolResult
        ), "A tool function must return a ToolResult object"

        for param in parameters[1:]:
            param_type = _resolve_param_type(param)

            if param_type.t not in get_args(_ToolParameterType) and not issubclass(
                param_type.t, enum.Enum
            ):
                raise AssertionError(
                    f"{param.name}: {param_type.t.__name__}: parameter type must be in {[t.__name__ for t in get_args(_ToolParameterType)]} or be a valid Enum type"
                )

            if issubclass(param_type.t, enum.Enum):
                assert all(
                    type(e.value) in get_args(EnumValueType) for e in param_type.t
                ), f"{param.name}: {param_type.t.__name__}: Enum values must be in {[t.__name__ for t in get_args(EnumValueType)]}"

    def _describe_parameters(func: ToolFunction) -> dict[str, ToolParameter]:
        type_to_param_type: dict[type[_ToolParameterType], ToolParameterType] = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean",
        }

        parameters = list(inspect.signature(func).parameters.values())
        parameters = parameters[1:]  # Skip tool context parameter

        param_descriptions = {}

        for p in parameters:
            param_type_info = _resolve_param_type(p)
            param_type = param_type_info.t

            if param_type in type_to_param_type:
                tool_param = ToolParameter(type=type_to_param_type[param_type])
            elif issubclass(param_type, enum.Enum):
                tool_param = ToolParameter(type="string", enum=[e.value for e in param_type])
            else:
                raise ValueError(f"Unsupported parameter type: {param_type}")

            param_descriptions[p.name] = tool_param

        return param_descriptions

    def _find_required_params(func: ToolFunction) -> list[str]:
        parameters = list(inspect.signature(func).parameters.values())
        parameters = parameters[1:]  # Skip tool context parameter
        return [p.name for p in parameters if p.annotation.__name__ != "Optional"]

    def decorator(func: ToolFunction) -> ToolEntry:
        _ensure_valid_tool_signature(func)

        entry = ToolEntry(
            tool=Tool(
                creation_utc=datetime.now(timezone.utc),
                name=kwargs.get("name") or func.__name__,
                description=func.__doc__ or "",
                parameters=_describe_parameters(func),
                required=_find_required_params(func),
                consequential=kwargs.get("consequential") or False,
            ),
            function=func,
        )

        return entry

    return decorator


@overload
def tool(
    **kwargs: Unpack[_ToolDecoratorParams],
) -> Callable[[ToolFunction], ToolEntry]: ...


@overload
def tool(func: ToolFunction) -> ToolEntry: ...


def tool(
    func: ToolFunction | None = None,
    **kwargs: Unpack[_ToolDecoratorParams],
) -> ToolEntry | Callable[[ToolFunction], ToolEntry]:
    if func:
        return _tool_decorator_impl()(func)
    else:
        return _tool_decorator_impl(**kwargs)


class ListToolsResponse(DefaultBaseModel):
    tools: list[Tool]


class ReadToolResponse(DefaultBaseModel):
    tool: Tool


class CallToolRequest(DefaultBaseModel):
    agent_id: str
    session_id: str
    arguments: dict[str, _ToolParameterType]


class PluginServer:
    def __init__(
        self,
        tools: Sequence[ToolEntry],
        port: int = 8089,
        host: str = "0.0.0.0",
    ) -> None:
        self.tools = {entry.tool.name: entry for entry in tools}
        self.host = host
        self.port = port
        self.url = f"http://{self.host}:{self.port}"

        self._server: Optional[uvicorn.Server] = None

    async def __aenter__(self) -> PluginServer:
        self._task = asyncio.create_task(self.serve())

        start_timeout = 5
        sample_frequency = 0.1

        for _ in range(int(start_timeout / sample_frequency)):
            await asyncio.sleep(sample_frequency)

            if self.started():
                return self

        raise TimeoutError()

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> bool:
        try:
            await self._task
        except asyncio.CancelledError:
            pass

        return False

    async def serve(self) -> None:
        app = self._create_app()

        config = uvicorn.Config(
            app,
            host=self.host,
            port=self.port,
            log_level="info",
        )

        self._server = uvicorn.Server(config)

        await self._server.serve()

    async def shutdown(self) -> None:
        if server := self._server:
            server.should_exit = True

    def started(self) -> bool:
        if self._server:
            return self._server.started
        return False

    def _create_app(self) -> FastAPI:
        app = FastAPI()

        @app.get("/tools")
        async def list_tools() -> ListToolsResponse:
            return ListToolsResponse(tools=[t.tool for t in self.tools.values()])

        @app.get("/tools/{name}")
        async def read_tool(name: str) -> ReadToolResponse:
            return ReadToolResponse(tool=self.tools[name].tool)

        @app.post("/tools/{name}/calls")
        async def call_tool(
            name: str,
            request: CallToolRequest,
        ) -> StreamingResponse:
            end = asyncio.Event()
            chunks_received = asyncio.Semaphore(value=0)
            lock = asyncio.Lock()
            chunks: list[str] = []

            async def chunk_generator(
                result_future: Awaitable[ToolResult],
            ) -> AsyncIterator[str]:
                while True:
                    end_future = asyncio.ensure_future(end.wait())
                    chunks_received_future = asyncio.ensure_future(chunks_received.acquire())

                    await asyncio.wait(
                        [end_future, chunks_received_future],
                        return_when=asyncio.FIRST_COMPLETED,
                    )

                    if chunks_received_future.done():
                        async with lock:
                            next_chunk = chunks.pop(0)
                        yield next_chunk
                        # proceed to next potential acquire/end,
                        # skipping the end-check, otherwise
                        # we may skip emitted chunks.
                        continue
                    else:
                        # Release the acquire we performed to skip it
                        chunks_received.release()
                        await chunks_received_future

                    if end_future.done():
                        try:
                            result = await result_future

                            final_result_chunk = json.dumps(
                                {
                                    "data": result.data,
                                    "metadata": result.metadata,
                                    "control": result.control,
                                }
                            )

                            yield final_result_chunk
                        except Exception as exc:
                            yield json.dumps({"error": str(exc)})

                        return
                    else:
                        end_future.cancel()
                        await asyncio.gather(end_future, return_exceptions=True)

            async def emit_message(message: str) -> None:
                async with lock:
                    chunks.append(json.dumps({"message": message}))
                chunks_received.release()

            async def emit_status(
                status: SessionStatus,
                data: JSONSerializable,
            ) -> None:
                async with lock:
                    chunks.append(json.dumps({"status": status, "data": data}))
                chunks_received.release()

            context = ToolContext(
                agent_id=request.agent_id,
                session_id=request.session_id,
                emit_message=emit_message,
                emit_status=emit_status,
            )

            func = self.tools[name].function
            func_params = inspect.signature(func).parameters
            converted_arguments = {
                param_name: func_params[param_name].annotation(arg_value)
                for param_name, arg_value in request.arguments.items()
            }

            result = self.tools[name].function(context, **converted_arguments)  # type: ignore

            result_future: asyncio.Future[ToolResult]

            if inspect.isawaitable(result):
                result_future = asyncio.ensure_future(result)
            else:
                result_future = asyncio.Future[ToolResult]()
                result_future.set_result(result)

            result_future.add_done_callback(lambda _: end.set())

            return StreamingResponse(
                content=chunk_generator(result_future),
                media_type="text/plain",
            )

        return app
