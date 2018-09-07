from functools import reduce
from subprocess import getstatusoutput
from typing import Dict, List, NamedTuple, Optional


class ShellCommandResult(NamedTuple):
    """shell commandの実行結果."""
    code: int
    value: str


def _add_command(lhs: str, rhs: str) -> str:
    """shell commandを結合(&&)する.

    :param lhs:
    :param rhs:
    :return: 'lhs && rhs'
    """
    return lhs + ' && ' + rhs


def execute(commands: List[str]) -> ShellCommandResult:
    """shell commandの配列から 'A && B && C && ...' を生成し実行する.

    :param commands: 実行するshell commandの配列
    :return: 実行結果
    """
    output = getstatusoutput(reduce(_add_command, commands))
    return ShellCommandResult(code=output[0], value=output[1])
