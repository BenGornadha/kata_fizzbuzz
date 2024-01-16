import unittest


class FizzConverter:
    def convert(self, number: int) -> str:
        if number % 3 == 0:
            return "Fizz"
        return str(number)


class MyTestCase(unittest.TestCase):
    def test_fizz_convert_nothing_when_number_is_not_divisible_by_3(self):
        fizz_converter = FizzConverter()
        one = 1

        self.assertEqual("1", fizz_converter.convert(number=one))

    def test_fizz_convert_to_string_Fizz_when_number_is_divisible_by_3(self):
        fizz_converter = FizzConverter()
        three = 3

        self.assertEqual("Fizz", fizz_converter.convert(number=three))
