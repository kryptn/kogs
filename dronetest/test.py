import unittest

class TestTest(unittest.TestCase):

    def test_math(self):
        self.assertEqual(1, 1)

    def test_add(self):
        self.assertEqual(1+1, 2)

    def test_sub(self):
        self.assertEqual(2-1, 1)

if __name__ == '__main__':
    unittest.main()
