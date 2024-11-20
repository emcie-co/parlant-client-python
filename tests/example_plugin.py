import asyncio
import sys

from parlant.core.tools import ToolResult, ToolContext
from parlant.core.services.tools.plugins import tool, PluginServer

PLUGIN_PORT = 8002
PLUGIN_ADDRESS = f"http://127.0.0.1:{PLUGIN_PORT}"


@tool
async def toolset_decription(context: ToolContext, question: str) -> ToolResult:
    return ToolResult("This plugin provides demo tools")


@tool
async def flip_coin(context: ToolContext, question: str) -> ToolResult:
    return ToolResult(data="Heads" if ord(context.agent_id[0]) % 2 else "Tails")


@tool
async def roll_die(context: ToolContext, question: str) -> ToolResult:
    return ToolResult(data=1 + ord(context.agent_id[0]) % 6)


async def main(port: int) -> None:
    print(f"Starting `randoms` plugin on port={port}")
    async with PluginServer(
        port=port,
        tools=[toolset_decription, flip_coin, roll_die],
    ):
        print("Running...")


if __name__ == "__main__":
    port = PLUGIN_PORT
    try:
        port = int(sys.argv[1])
    finally:
        asyncio.run(main(port))
