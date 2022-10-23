input = 3

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    # n이 fibo_memo의 key로 존재하면
    if n in fibo_memo:
        # n에 대응되는 value를 바로 반환한다.
        return fibo_memo[n]
    # n이 존재하지 않을 경우, n-1, n-2에 대한 함수를 각각 호출한다.
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    # nth_value를 n번째 value로 저장한다.
    fibo_memo[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming(input, memo))
