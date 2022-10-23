import math
input = "0111010101"

# 연속된 숫자가 바뀔 때마다 switch 값을 1씩 증가시킨다.
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    switch = 0
    criteria = string[0]
    for i in string:
        if i == criteria:
            continue
        else:
            switch += 1
            criteria = i
    # "010101"처럼 마지막 숫자를 뒤집는 경우 switch 값이 홀수가 되므로, 올림 함수를 사용함.
    return math.ceil(switch/2)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
