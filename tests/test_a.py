import dataclasses
import unittest


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


class StringNumber:
    def __init__(self, number: int):
        self._number = number

    def __repr__(self) -> str:
        return str(self._number)

    def __eq__(self, other) -> bool:
        return isinstance(other, StringNumber) and self._number == other._number


class FizzBuzzFactory:
    def convert_from(self, number: int) -> Fizz | Buzz | FizzBuzz | StringNumber | FizzBuzzBuzz:
        if self._3_and_5_in(number=number) and self._is_divisible_by_5(number=number):
            return FizzBuzzBuzz()
        if self._3_and_5_in(number=number):
            return FizzBuzz()
        if self._is_divisible_by_3(number=number) and self._is_divisible_by_5(number=number):
            return FizzBuzz()
        if self._is_divisible_by_3(number=number):
            return Fizz()
        if self._is_divisible_by_5(number=number):
            return Buzz()
        if self._3_in(number=number):
            return Fizz()
        if self._5_in(number=number):
            return Buzz()
        return StringNumber(number)

    def _3_and_5_in(self, number: int) -> bool:
        return self._3_in(number) and self._5_in(number)

    def _5_in(self, number):
        return "5" in str(number)

    def _3_in(self, number):
        return "3" in str(number)

    def _is_divisible_by_5(self, number: int) -> bool:
        return number % 5 == 0

    def _is_divisible_by_3(self, number: int) -> bool:
        return number % 3 == 0


class MyTestCase(unittest.TestCase):
    def test_number_one_is_one(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=1)
        self.assertEqual(StringNumber(1), sut)

    def test_divisible_by_3_is_Fizz(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=3)
        self.assertEqual(Fizz(), sut)
        self.assertEqual("Fizz", f"{sut}")
        sut = fizz_buzz.convert_from(number=9)
        self.assertEqual(Fizz(), sut)

    def test__divisible_by_5_if_buzz(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=5)
        self.assertEqual(Buzz(), sut)
        self.assertEqual("Buzz", f"{sut}")
        sut = fizz_buzz.convert_from(number=10)
        self.assertEqual(Buzz(), sut)

    def test__divisible_by_5_and_3_is_fizz_buzz(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=15)
        self.assertEqual(FizzBuzz(), sut)
        self.assertEqual("FizzBuzz", f"{sut}")

    def test_v2(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=53)
        self.assertEqual(FizzBuzz(), sut)

    def test_v22(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=35)
        self.assertEqual(FizzBuzzBuzz(), sut)

    def test_v222(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=43)
        self.assertEqual(Fizz(), sut)

    def test_v2222(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=98)
        self.assertEqual(StringNumber(98), sut)
