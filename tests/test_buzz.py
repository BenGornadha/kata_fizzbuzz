import unittest


class BuzzConverter:
    def convert(self, number: int) -> str:
        if number % 5 == 0:
            return "Buzz"
        return str(number)


class MyTestCase(unittest.TestCase):
    def test_buzz_convert_nothing_when_number_is_not_divisible_by_5(self):
        buzz_converter = BuzzConverter()
        one = 1

        self.assertEqual("1", buzz_converter.convert(number=one))

    def test_buzz_convert_to_string_Fizz_when_number_is_divisible_by_3(self):
        fizz_converter = BuzzConverter()
        five = 5

        self.assertEqual("Buzz", fizz_converter.convert(number=five))
