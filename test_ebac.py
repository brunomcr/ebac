import unittest
from BubbleSort import bubble_sorte





class BubbleSort(unittest.TestCase):

    def sort(self):
        unsorted_list = [54, 78, 12, 5, 1234, 87, 9]
        expected_list = [5, 9, 12, 54, 78, 87, 1234]
        unsorted_list = bubble_sorte(unsorted_list)
        self.assertEqual(unsorted_list, expected_list)

if __name__ == '__main__':
    unittest.main()