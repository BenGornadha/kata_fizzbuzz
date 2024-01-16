import dataclasses
import unittest


@dataclasses.dataclass
class Fizz:
    value = "Fizz"


@dataclasses.dataclass
class Buzz:
    value = "Buzz"


@dataclasses.dataclass
class FizzBuzz:
    value = "FizzBuzz"


class FizzBuzzFactory:
    def convert_from(self, number: int) -> Fizz | Buzz | FizzBuzz | str:
        if self._is_divisible_by_3(number=number) and self._is_divisible_by_5(number=number):
            return FizzBuzz()
        if self._is_divisible_by_3(number):
            return Fizz()
        if self._is_divisible_by_5(number):
            return Buzz()
        return str(number)

    def _is_divisible_by_5(self, number: int) -> bool:
        return number % 5 == 0

    def _is_divisible_by_3(self, number: int) -> bool:
        return number % 3 == 0


class MyTestCase(unittest.TestCase):
    def test_number_one_is_one(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=1)
        self.assertEqual("1", sut)

    def test_divisible_by_3_is_Fizz(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=3)
        self.assertEqual(Fizz(), sut)
        sut = fizz_buzz.convert_from(number=9)
        self.assertEqual(Fizz(), sut)

    def test__divisible_by_5_if_buzz(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=5)
        self.assertEqual(Buzz(), sut)
        sut = fizz_buzz.convert_from(number=10)
        self.assertEqual(Buzz(), sut)

    def test__divisible_by_5_and_3_is_fizz_buzz(self):
        fizz_buzz = FizzBuzzFactory()
        sut = fizz_buzz.convert_from(number=15)
        self.assertEqual(FizzBuzz(), sut)
