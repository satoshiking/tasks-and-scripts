"""
We need to find the largest square comprising of all ones
in the given m x n matrix. In other words we need to find the largest set
of connected ones in the given matrix that forms a square
"""
import unittest


def check_boxes(mat, i, j):
    sq_max = min([len(mat) - i, len(mat[0]) - j])
    result = 0
    for n in range(1, sq_max+1):
        if set([mat[x][y] for x in range(i, i+n) for y in range(j, j+n)]) == {1}:
            result = n
        else:
            break
    return result


def find_sq(mat):
    return (max([check_boxes(mat, i, j) for i in range(len(mat))
            for j in range(len(mat[0]))]))**2 if mat else 0


class Test_find_maximum_square(unittest.TestCase):
    def test_zero_matrix(self):
        mat = []
        self.assertEqual(find_sq(mat), 0)

    def test_all_ones_matrix(self):
        mat = [
                  [1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]
        ]
        self.assertEqual(find_sq(mat), 9)

    def test_standart1_matrix(self):
        mat = [
               [0, 1, 0, 1, 0, 1],
               [0, 0, 1, 1, 1, 1],
               [0, 1, 1, 1, 1, 1],
               [0, 0, 1, 1, 1, 1],
               [0, 1, 1, 1, 1, 1],
               [0, 1, 0, 1, 0, 1],
        ]
        self.assertEqual(find_sq(mat), 16)

    def test_standart2_matrix(self):
        mat = [
               [0, 1, 0, 1, 0, 1],
               [0, 0, 1, 1, 1, 1],
               [0, 1, 1, 0, 1, 1],
               [0, 0, 1, 0, 1, 1],
               [0, 1, 1, 1, 1, 1],
               [0, 1, 0, 1, 1, 1],
        ]
        self.assertEqual(find_sq(mat), 4)

    def test_rectangle1_matrix(self):
        mat = [
               [0, 1, 1, 1, 0, 1],
               [0, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(find_sq(mat), 4)

    def test_rectangle2_matrix(self):
        mat = [
               [0, 1],
               [0, 1],
               [1, 1],
               [0, 1],
               [0, 1],
               [1, 1],
               [0, 1],
        ]
        self.assertEqual(find_sq(mat), 1)


if __name__ == '__main__':
    unittest.main()
