import unittest
import os.path


class Autograder(unittest.TestCase):
    def test_result(self):
        # check if the file `causal_testing.png` exists
        self.assertEqual(True, os.path.isfile('causal_testing.png'))
        self.assertEqual(True, os.path.getsize('causal_testing.png') > 0)


if __name__ == '__main__':
    unittest.main()
