#Testing code 

import unittest

class TestSum(unittest.TestCase):

    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_float(self):
        data = [1.0, 2.0, 3.0]
        result = sum(data)
        self.assertEqual(result, 6.0)

if __name__ == "__main__":
    unittest.main()
