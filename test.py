import unittest
from my_sum import maximal_element
class TestMaxElement(unittest.TestCase):
    def test_list_1(self):
        data = [1, 2, 3, 1, 54, -56, -8521, 4156 ,947]
        result = maximal_element(data)
        self.assertEqual(result, 7)
    def test_list_2(self):
        data = []
        result = maximal_element(data)
        self.assertEqual(result, -1)
    def test_list_3(self):
        data = [1]
        result = maximal_element(data)
        self.assertEqual(result, 0)
    def test_list_4(self):
        data = [1, 1, 1, 1, 1]
        result = maximal_element(data)
        self.assertEqual(result, 0)
    def test_list_5(self):
        data = [1, -1651, 0, 16, 45, -6864, 23, 3564]
        result = maximal_element(data)
        self.assertEqual(result, 7)
    def test_list_6(self):
        data = [1146541, 213, -4546156, 0, 15]
        result = maximal_element(data)
        self.assertEqual(result, 0)
if __name__ == '__main__':
    unittest.main()
