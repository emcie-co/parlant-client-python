import asyncio
from contextlib import contextmanager
import os
import signal
import subprocess
from dataclasses import dataclass
from pathlib import Path
import sys
import time
from typing import Any, Iterator


def is_server_running(port: int) -> bool:
    if _output_view := subprocess.getoutput(f"lsof -i:{port}"):
        print(_output_view)
        return True

    return False


async def run_cli(*args: str, **kwargs: Any) -> asyncio.subprocess.Process:
    exec_args = [
        "poetry",
        "run",
    ] + list(args)
    print(f"Running: {exec_args}")
    return await asyncio.create_subprocess_exec(*exec_args, **kwargs)


@dataclass(frozen=True)
class ContextOfTest:
    home_dir: Path


@contextmanager
def run_cli2(
    context: ContextOfTest,
    args: list[str],
) -> Iterator[subprocess.Popen[str]]:
    caught_exception: Exception | None = None

    try:
        with subprocess.Popen(
            args=args,
            text=True,
            stdout=sys.stdout,
            stderr=sys.stdout,
            env={**os.environ, "PARLANT_HOME": context.home_dir.as_posix()},
        ) as process:
            try:
                yield process
            except Exception as exc:
                caught_exception = exc

            if process.poll() is not None:
                return

            process.send_signal(signal.SIGINT)

            for _ in range(5):
                if process.poll() is not None:
                    return
                time.sleep(0.5)

            process.terminate()

            for _ in range(5):
                if process.poll() is not None:
                    return
                time.sleep(0.5)

            print(
                "Server process had to be killed. stderr="
                + (process.stderr and process.stderr.read() or "None")
            )

            process.kill()
            process.wait()

    finally:
        if caught_exception:
            raise caught_exception
