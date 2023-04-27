import unittest
from sum import my_sum
class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(my_sum(1, 2), 3)
        self.assertEqual(my_sum(0, 0), 0)
        self.assertEqual(my_sum(-1, 1), 0)
if __name__ == "__main__":
    unittest.main()
