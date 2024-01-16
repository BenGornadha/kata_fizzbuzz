from tests.test_fizzbuzz import FizzBuzz

if __name__ == '__main__':
    input = [i for i in range(1, 101)]
    fizz_buzz = FizzBuzz()
    with open("result.txt", "w") as fd:
        for number in input:
            output = fizz_buzz.convert_from(number=number)
            fd.writelines(f"{output}\n")
