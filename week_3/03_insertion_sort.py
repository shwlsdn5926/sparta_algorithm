input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(i+1):
            if array[i - j + 1] < array[i - j]:
                array[i - j + 1], array[i - j] = array[i - j], array[i - j + 1]
            else:
                break
    return


insertion_sort(input)
print(input)
