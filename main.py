from tests.test_fizzbuzz import FizzBuzzFactory

if __name__ == '__main__':
    # Let's go for first part of FizzBuzz
    #For second version we just hae to relaunch.
    input = [a_number for a_number in range(1, 101)]
    fizz_buzz_factory = FizzBuzzFactory()
    with open("result_second_version.txt", "w") as fd:
        for a_number in input:
            result_to_write = fizz_buzz_factory.convert(number=a_number)
            fd.writelines(str(result_to_write) + "\n")

