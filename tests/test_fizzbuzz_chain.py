import unittest

from chain_of_responsibility.fizz_buzz import Buzz, Request, Fizz


class TestChain(unittest.TestCase):

    def test_fizzbuzz_chained_to_buzz2(self):
        b = Buzz()
        request = Request(input=5)
        sut = b.handle(request)

        self.assertEqual(Request(input=5, output="Buzz"), sut)

    def test_fizzbuzz_chained_to_buzz3(self):
        fizz = Fizz()
        request = Request(input=3)
        sut = fizz.handle(request)

        self.assertEqual(Request(input=3, output="Fizz"), sut)

    def test_fizzbuzz_chained_to_buzz33(self):
        fizz = Fizz()
        buzz = Buzz()
        fizz.set_next_object(an_object=buzz)

        request = Request(input=15)
        sut = fizz.handle(request)

        self.assertEqual(Request(input=15, output="FizzBuzz"), sut)

    def test_fizzbuzz_default_ended_link_is_convert_to_string_v2(self):
        fizz = Fizz()

        request = Request(input=1)
        sut = fizz.handle(request)

        self.assertEqual(Request(input=1, output="1"), sut)

    def test_order_of_links_is_important_buff_follow_by_a_fizz(self):
        buzz = Buzz()
        buzz.set_next_object(Fizz())

        request = Request(input=3)
        sut = buzz.handle(request)

        self.assertEqual(Request(input=3, output="Fizz"), sut)

    def test_order_of_links_buzz_and_after_fizz_with_15(self):
        buzz = Buzz()
        buzz.set_next_object(Fizz())

        request = Request(input=15)
        sut = buzz.handle(request)

        self.assertEqual(Request(input=15, output="FizzBuzz"), sut)

    def test_order_of_links_fizz_and_after_buzz_with_15(self):
        fizz = Fizz()
        fizz.set_next_object(Buzz())

        request = Request(input=15)
        sut = fizz.handle(request)

        self.assertEqual(Request(input=15, output="FizzBuzz"), sut)
