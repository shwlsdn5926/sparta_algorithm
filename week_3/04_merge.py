array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

n=len(array_a)
print(n)
def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1

    # array1의 마지막 원소를 array_c에 넣었으니 array1_index는 max_index보다 1 초과되었다.
    if array1_index == len(array1):
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1
    if array2_index == len(array2):
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
            array1_index += 1

    return array_c


print(merge(array_a, array_b))
