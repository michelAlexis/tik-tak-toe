import unittest

from tiktaktoe.utils.array_utils import star_equals

class ArrayUtilsTest(unittest.TestCase):

    def test_single_two_case(self):
        arr = [
            [1,1],
            [0,0]
        ]

        res = star_equals(arr, (0, 0), 2)
        self.assertListEqual(res, [(0,0), (0,1)])

    def test_empty(self):
        arr = [
            [0,0,0],
            [0,1,0],
            [0,1,0]
        ]

        res = star_equals(arr, (1, 1), 3)
        self.assertEquals(len(res), 0)

    def test_single_result_star(self):
        arr = [
            [0,0,0],
            [0,1,0],
            [0,1,0]
        ]

        res = star_equals(arr, (1,1), 2)
        self.assertListEqual(res, [(1,1), (2,1)])

    def test_single_middle_all_row(self):
        # Vertical
        arr = [
            [0,1,0],
            [0,1,0],
            [0,1,0]
        ]

        res = star_equals(arr, (0,1), 3)
        self.assertListEqual(res, [(0,1), (1,1), (2,1)])

        res = star_equals(arr, (1,1), 3)
        self.assertListEqual(res, [(0,1), (1,1), (2,1)])

        res = star_equals(arr, (2,1), 3)
        self.assertListEqual(res, [(0,1), (1,1), (2,1)])

        # horizontal
        arr = [
            [0,0,0],
            [1,1,1],
            [0,0,0]
        ]

        res = star_equals(arr, (1,0), 3)
        self.assertListEqual(res, [(1,0), (1,1), (1,2)])

        res = star_equals(arr, (1,1), 3)
        self.assertListEqual(res, [(1,0), (1,1), (1,2)])

        res = star_equals(arr, (1,2), 3)
        self.assertListEqual(res, [(1,0), (1,1), (1,2)])


if __name__ == "__main__":
    unittest.main()