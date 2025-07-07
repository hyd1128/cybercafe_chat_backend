#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import time
from contextlib import contextmanager
from typing import Callable


@contextmanager
def my_context_manager():
    print("进入上下文管理器")
    try:
        yield
    finally:
        print("退出上下文管理器")


with my_context_manager():
    print("我正在上下文管理器对象中")


@contextmanager
def custom_context_manage() -> Callable:
    print("上下文管理器上")

    def inner_function(sleep_time_: int) -> None:
        print(f"我准备沉睡 {sleep_time_} s")
        time.sleep(sleep_time_)

    yield inner_function

    print("上下文管理器之外")


with custom_context_manage() as context_:
    context_(3)

