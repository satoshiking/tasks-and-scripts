import unittest


# Selection sort algorithm
def get_smallest(list_to_sort):
    smallest = list_to_sort[0]
    smallest_index = 0
    for i in range(1, len(list_to_sort)):
        if list_to_sort[i] < smallest:
            smallest = list_to_sort[i]
            smallest_index = i
    return smallest_index


def sort_by_selection(list_to_sort):
    list_sorted = []
    for i in range(len(list_to_sort)):
        list_sorted.append(list_to_sort.pop(get_smallest(list_to_sort)))
    return list_sorted


# Quick sort algorithm
def qsort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        opornii = list_to_sort.pop(len(list_to_sort) // 2)
        lower = [i for i in list_to_sort if i <= opornii]
        higher = [i for i in list_to_sort if i > opornii]
        return qsort(lower) + [opornii] + qsort(higher)


def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1
    guess = (low + high) // 2

    while guess <= high:
        if sorted_list[guess] == item:
            return guess
        elif sorted_list[guess] > item:
            high = guess - 1
            guess = (low + high) // 2
        elif sorted_list[guess] < item:
            low = guess + 1
            guess = (low + high) // 2


class TestSortingAlgorithms(unittest.TestCase):
    def test_sort_by_selection(self):
        self.assertEqual(sort_by_selection([10, 20, 35, 44, 3, 8]), [3, 8, 10, 20, 35, 44])

    def test_sort_by_selection_sorted(self):
        self.assertEqual(sort_by_selection([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sort_by_selection_sorted_decending(self):
        self.assertEqual(sort_by_selection([96, 37, 14, 8, 3, -5]), [-5, 3, 8, 14, 37, 96])

    def test_sort_by_selection_empty(self):
        self.assertEqual(sort_by_selection([]), [])

    def test_qsort(self):
        self.assertEqual(qsort([10, 20, 35, 44, 3, 8]), [3, 8, 10, 20, 35, 44])

    def test_qsort_sorted(self):
        self.assertEqual(qsort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_qsort_decending(self):
        self.assertEqual(qsort([96, 37, 14, 8, 3, -5]), [-5, 3, 8, 14, 37, 96])

    def test_qsort_equal(self):
        self.assertEqual(qsort([2,2,2,2]), [2,2,2,2])

    def test_qsort_empty(self):
        self.assertEqual(qsort([]), [])


class TestSearchingAlgorithms(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search(['a', 'b', 'c', 'd' ,'e', 'f'], 'c'), 2)

    def test_binary_search_first(self):
        self.assertEqual(binary_search(['a', 'b', 'c', 'd' ,'e', 'f'], 'a'), 0)

    def test_binary_search_last(self):
        self.assertEqual(binary_search(['a', 'b', 'c', 'd' ,'e', 'f'], 'f'), 5)

    def test_binary_search_one_element(self):
        self.assertEqual(binary_search(['a'], 'a'), 0)


if __name__ == '__main__':
    unittest.main()