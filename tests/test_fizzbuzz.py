import dataclasses
import unittest
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
        if self._5_and_3_in(number) and self._is_divisible_by_5(number=number):
            return FizzBuzzBuzz()
        if self._is_fizz_buzz(number=number):
            return FizzBuzz()
        if self._is_fizz(number=number):
            return Fizz()
        if self._is_buzz(number):
            return Buzz()

        return NumberString(number=number)

    def _is_buzz(self, number):
        return self._is_divisible_by_5(number=number) or self._5_in(number=number)

    def _is_fizz(self, number: int) -> bool:
        return self._is_divisible_by_3(number=number) or self._3_in(number=number)

    def _is_fizz_buzz(self, number: int):
        return self._5_and_3_in(number) or self._is_divisible_by_5_and_3(number=number)

    def _5_and_3_in(self, number: int) -> bool:
        return self._5_in(number) and self._3_in(number=number)

    def _5_in(self, number :int) -> bool:
        return "5" in str(number)

    def _3_in(self, number: int) -> bool:
        return "3" in str(number)

    def _is_divisible_by_5_and_3(self, number: int) -> bool:
        return self._is_divisible_by_5(number=number) and self._is_divisible_by_3(number=number)

    def _is_divisible_by_5(self, number: int) -> bool:
        return number % 5 == 0

    def _is_divisible_by_3(self, number: int) -> bool:
        return number % 3 == 0


class MyTestCase(unittest.TestCase):
    def test_number_one_is_not_converted(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=1)

        self.assertEqual(NumberString(number=1), sut)

    def test_three_is_converted_to_string_Fizz(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=3)

        self.assertEqual(Fizz(), sut)
        self.assertEqual("Fizz", f"{sut}")

    def test_five_is_converted_to_string_Buzz(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=5)

        self.assertEqual(Buzz(), sut)
        self.assertEqual("Buzz", f"{sut}")

    def test_fifteen_is_converted_to_string_FizzBuzz(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=15)

        self.assertEqual(FizzBuzz(), sut)
        self.assertEqual("FizzBuzz", f"{sut}")

    def test_number_with_3_in_it_but_not_divisible_is_fizz(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=13)
        self.assertEqual(Fizz(), sut)

    def test_number_with_5_and_3_but_not_divisible_is_fizz_buzz(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=53)

        self.assertEqual(FizzBuzz(), sut)

    def test_number_with_3_and_5_and_divisible_by_5_is_FizzBuzzBuzz(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=35)

        self.assertEqual(FizzBuzzBuzz(), sut)
        self.assertEqual("FizzBuzzBuzz", f"{sut}")

    def test_normal_case(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=98)

        self.assertEqual(NumberString(98), sut)

    def test_has_five_in(self):
        fizz_buzz = FizzBuzzFactory()

        sut = fizz_buzz.convert(number=52)

        self.assertEqual(Buzz(), sut)
