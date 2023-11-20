import unittest
import os
import sys

test_directory = os.path.join(os.path.dirname(__file__), 'tests')


def run_specific_test(datastructure):
    test_loader = unittest.TestLoader()
    test_suit = test_loader.loadTestsFromName(f"tests.test_{datastructure}", module=None)
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suit)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <function_name>")
        sys.exit(1)

    name = "".join([word.capitalize() for word in sys.argv[1].split("_")])
    run_specific_test(name)
