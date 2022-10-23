input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        start_index = i
        for j in range(n - i):
            if array[start_index] > array[i + j]:
                start_index = i + j
        array[i], array[start_index] = array[start_index], array[i]
    return


selection_sort(input)
print(input)
