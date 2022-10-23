input = [6,6,7]


def find_max_num(array):
    # 가장 큰 수를 저장할 변수 max_num 지정하기
    max_num = array[0]
    for num in array:
        # 다음 조건에 해당하는 경우에만 max_num 값 변경
        if num > max_num:
            max_num = num
    # 반복이 모두 끝난 후 max_num 값 출력
    return max_num


result = find_max_num(input)
print(result)
