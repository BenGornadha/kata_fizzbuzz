from tests.test_a import FizzBuzzFactory

if __name__ == '__main__':
    input = [i for i in range(1, 101)]
    factory = FizzBuzzFactory()
    with open("result.txt", "w") as fd:
        for number in input:
            output = factory.convert_from(number=number)
            fd.writelines(f"{output}\n")
