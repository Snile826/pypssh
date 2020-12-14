#!/bin/env python
import glob
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import as_completed
import re
import sys
import platform
import pprint
from string import Template
import paramiko
from pathlib import Path
import yaml
import logging
from typing import Union, Optional, List, Callable
import click


logging.basicConfig(level=logging.ERROR,format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class Mode(Enum):
    """
    该程序的反馈有两种模式
      - 便于人类阅读的普通模式
      - 便于程序交互的命令行模式
    """
    PLAIN = 0
    JSON = 1

@dataclass
class Session:
    """
    会话类
    """
    hostname: str = "localhost"
    user: str = "root"
    port: int = 22
    passwd:str = ""
    pkfile: str = ""
    pkpasswd: str = ""
    groups: List[str] = field(default_factory=list)

@dataclass
class SSHResult:
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    returncode:int = 0
    exception: Optional[Exception] = None
    content: Union[bytes, str, None] = None

def concurrent(func:Callable, tasks:list):
    future_list = list()
    result_list = list()
    for task in tasks:
        future_list.append(self.executor.submit(func, *task))
    for future in as_completed(future_list):
        result_list.append(future.result())
    return result_list

ALL_HOST = list()
SELECTED_HOST = list()
MODE=Mode.PLAIN

@click.group()
def cli(inventory, level, mode, config):
    pass

@cli.group()
def config():
    pass

@config.command()
def add_host():
    pass

@config.command()
def del_host():
    pass


@cli.command()
def execute():
    pass

@cli.command()
@click.argument('local_file', type=click.types.Path(exists=True))
@click.argument('remote_file', type=click.types.Path())
def put(local_file, remote_file):
    """
    为目标批量上传文件
    """
    pass

@cli.command()
@click.argument('remote_file', type=click.types.Path())
@click.argument('local_file', type=click.types.Path())
def pull(remote_file, local_file):
    """
    为目标批量下载文件
    """
    pass


@cli.command()
def test():
    pass


# 远程执行脚本文件，可以从配置文件加载变量，可以读参数变量
@cli.command()
def execfile(ctx, script_file, json, template, script_arg, env, attachment, workdir):
    pass


@cli.command()
def version():
    addr = "https://github.com/Snile826/pypssh"
    vno = "v0.2.0"
    interrupt_version = "Python " + ' '.join(sys.version.split('\n'))
    print(
        "\n".join
        ([
            f"地址: {addr}",
            f"版本号: {vno}",
            f"解释器版本: {interrupt_version}",
            f"发行版: {platform.platform()}"
        ])
    )

if __name__ == '__main__':
    cli()
