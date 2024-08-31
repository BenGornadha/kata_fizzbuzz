import dataclasses
from typing import Any


class NumberString:
    def __init__(self, number: int):
        self._number = number

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, NumberString) and self._number == other._number

    def __repr__(self) -> str:
        return str(self._number)


@dataclasses.dataclass
class Fizz:
    def __repr__(self) -> str:
        return self.__class__.__name__


@dataclasses.dataclass
class Buzz:
    def __repr__(self) -> str:
        return self.__class__.__name__


@dataclasses.dataclass
class FizzBuzz:
    def __repr__(self) -> str:
        return self.__class__.__name__


@dataclasses.dataclass
class FizzBuzzBuzz:
    def __repr__(self) -> str:
        return self.__class__.__name__


class FizzBuzzFactory:
    def convert(self, number: int) -> NumberString | Fizz | Buzz | FizzBuzz | FizzBuzzBuzz:
        if self._5_and_3_in(number) and self._is_divisible_by(divisor=5, number=number):
            return FizzBuzzBuzz()
        if self._is_fizz_buzz(number=number):
            return FizzBuzz()
        if self._is_fizz(number=number):
            return Fizz()
        if self._is_buzz(number):
            return Buzz()

        return NumberString(number=number)

    def _is_buzz(self, number: int) -> bool:
        return self._is_divisible_by(divisor=5, number=number) or self._value_in("5", number)

    def _is_fizz(self, number: int) -> bool:
        return self._is_divisible_by(divisor=3, number=number) or self._value_in("3", number)

    def _is_fizz_buzz(self, number: int):
        return self._5_and_3_in(number) or self._is_divisible_by_5_and_3(number=number)

    def _5_and_3_in(self, number: int) -> bool:
        return self._value_in("5", number) and self._value_in("3", number)

    def _value_in(self, value: str, number: int) -> bool:
        return value in str(number)

    def _is_divisible_by(self, divisor: int, number: int) -> bool:
        return number % divisor == 0

    def _is_divisible_by_5_and_3(self, number: int) -> bool:
        return self._is_divisible_by(divisor=5, number=number) and self._is_divisible_by(divisor=3, number=number)
