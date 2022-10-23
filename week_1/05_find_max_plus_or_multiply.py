# 페이스북 기출문제
input = [3, 2, 1, 5, 9, 7, 4]


def find_max_plus_or_multiply(array):
    mul_sum = 0
    for i in array:
        if i <= 1 or mul_sum <= 1:
            mul_sum += i
        else:
            mul_sum *= i
    return mul_sum


result = find_max_plus_or_multiply(input)
print(result)

# 문제에서 구해야 하는 것 : 값을 비교하는 것
# x와 +만을 이용하여 계산한 값은 총 몇 개일까?
# -> 모든 결과를 다 알아야 할까?
# 계산을 어떻게 수행할까?
# -> array의 첫 번째 숫자를 택한다.
# -> array의 두 번째 숫자와 더한 값을
# 배열의 각 숫자에 대해 다음 숫자를 곱하거나 더한다.
# -> 최소 N의 시간복잡도를 가진다.
# 선형 시간복잡도를 가지도록 하려면?
# 반복문을 1번만 돌리자.
# 조건문 하나만 이용하면 된다.
# 현재까지 계산한 값 또는 계산할 값이 1 이하라면?
# 더하는 게 무조건 이득이다.
# 그 외에는 곱하면 된다.

# 시간복잡도를 분석해보자.
# array의 길이 * 수행 조건2 -> N
