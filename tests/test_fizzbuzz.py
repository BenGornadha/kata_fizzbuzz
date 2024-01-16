import unittest

from tests.test_buzz import BuzzConverter
from tests.test_fizz import FizzConverter


class FizzBuzz:
    def __init__(self):
        self._fizz_converter = FizzConverter()
        self._buzz_converter = BuzzConverter()

    def convert(self, number: int) -> str:
        fizz = self._fizz_converter.convert(number=number)
        if fizz == str(number):
            buzz = self._buzz_converter.convert(number=number)
            return buzz
        if fizz == "Fizz":
            buzz = self._buzz_converter.convert(number=number)
            if buzz == "Buzz":
                return "FizzBuzz"
        return fizz

class MyTestCase(unittest.TestCase):
    def test_something(self):
        fizz_buzz = FizzBuzz()
        sut = fizz_buzz.convert(number=1)
        self.assertEqual("1", sut)

    def test_something2(self):
        fizz_buzz = FizzBuzz()
        sut = fizz_buzz.convert(number=3)
        self.assertEqual("Fizz", sut)

    def test_something3(self):
        fizz_buzz = FizzBuzz()
        sut = fizz_buzz.convert(number=5)
        self.assertEqual("Buzz", sut)

    def test_something4(self):
        fizz_buzz = FizzBuzz()
        sut = fizz_buzz.convert(number=15)
        self.assertEqual("FizzBuzz", sut)
