array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    mid = len(array) // 2
    if len(array) <= 1:
        return array
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
# merge(merge(merge(...,),merge(,)),merge(merge(,),merge(,)))
# merge(,)안에 merge(,) 두 개가 반복되는 구조
# 배열의 길이가 홀수인 경우, 길이가 짧은 쪽이 왼쪽, 긴 쪽이 오른쪽으로 나눠짐.


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))
