import unittest

from first_version.fizz_buzz import NumberString, Fizz, Buzz, FizzBuzz, FizzBuzzBuzz, FizzBuzzFactory


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
