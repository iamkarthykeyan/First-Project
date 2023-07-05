#Testing codes for app

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

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

