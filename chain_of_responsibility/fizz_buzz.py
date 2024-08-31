from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Request:
    input: int
    output: str = ""


class FizzBuzzLink(ABC):
    def __init__(self):
        self._next = None

    @abstractmethod
    def handle(self, value: Request) -> Request:
        raise NotImplemented

    def set_next_object(self, an_object: FizzBuzzLink) -> None:
        self._next = an_object

    def _call_next(self, value: Request) -> Request:
        if self._next:
            return self._next.handle(value)
        return value


class Fizz(FizzBuzzLink):
    def __init__(self):
        super().__init__()
        self._next: FizzBuzzLink = ConvertToString()

    def handle(self, value: Request) -> Request:
        if value.input % 3 == 0:
            value.output = "Fizz" + value.output

        return self._call_next(value)


class Buzz(FizzBuzzLink):
    def __init__(self):
        super().__init__()
        self._next: FizzBuzzLink = ConvertToString()

    def handle(self, value: Request) -> Request:
        if value.input % 5 == 0:
            value.output += "Buzz"

        return self._call_next(value)


class ConvertToString(FizzBuzzLink):

    def handle(self, value: Request) -> Request:
        if value.output == "":
            value.output = str(value.input)
        return value
