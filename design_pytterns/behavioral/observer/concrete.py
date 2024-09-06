from abc import ABC

from .observer import Observer


class AbstractCounter(Observer):
    def __init__(self, start: int = 0, increment: int = 1) -> None:
        self.value = start
        self.increment = increment


class Counter(AbstractCounter):
    def update(self) -> None:
        self.value += self.increment


class DoubleCounter(AbstractCounter):
    def update(self) -> None:
        self.value += 2 * self.increment
