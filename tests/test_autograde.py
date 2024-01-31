import unittest
import os.path
import hello


class TestAutograder(unittest.TestCase):
    def test_result(self):
        # check if the file `causal_testing.png` exists
        self.assertEqual(True, os.path.isfile('causal_testing.png'))
        self.assertEqual(True, os.path.getsize('causal_testing.png') > 0)

    def test_hello(self):
        # check if the file `causal_testing.png` exists
        self.assertEqual("Hello World", hello.say_hello())


if __name__ == '__main__':
    unittest.main()
