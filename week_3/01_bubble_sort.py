# 내가 구현한 코드 - 종료 조건 만족 시 배열 반환
input = [100, 56, -3, 32, 44]


def bubble_sort(array):
    swap_cnt = 0
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            swap_cnt += 1
    if swap_cnt == 0:
        return array
    bubble_sort(array)


bubble_sort(input)
print(input)

# 이중반복문(강사) - 버블정렬의 본질에 가까움
input = [100, 56, -3, 32, 44]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)
