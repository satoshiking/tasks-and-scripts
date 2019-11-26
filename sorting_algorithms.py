a = [10, 20, 35, 44, 3, 8]
b = []

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

#print(sort_by_selection(b))


# Quick sort algorithm
def qsort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        opornii = list_to_sort[len(list_to_sort) // 2]
        lower = [i for i in list_to_sort if i < opornii]
        higher = [i for i in list_to_sort if i > opornii]
        return qsort(lower) + [opornii] + qsort(higher)


print(qsort(a))