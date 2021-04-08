import unittest

from main import hello


class BasicTest(unittest.TestCase):

    def hello_test(self):
        self.assertEqual(hello(), "Hello, world!")
