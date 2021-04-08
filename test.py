import unittest

from main import hello, goodbye


class BasicTest(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, world!")

    def test_goodbye(self):
        self.assertEqual(goodbye(), "Goodbye!")


if __name__ == "__main__":
    unittest.main()