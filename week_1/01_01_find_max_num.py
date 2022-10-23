input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이중반복문에서 break에 한번도 걸리지 않은 num값을 찾는 게 목표!!
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
