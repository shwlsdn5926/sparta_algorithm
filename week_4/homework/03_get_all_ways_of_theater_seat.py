seat_count = 10
vip_seat_array = [2, 6, 9]

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    answer = 1
    fixed_num = 1
    for i in fixed_seat_array:
        difference = i - fixed_num
        answer *= fibo_dynamic_programming(difference, memo)
        fixed_num = i + 1
    last_fixed_num = total_count - fixed_num + 1
    answer *= fibo_dynamic_programming(last_fixed_num, memo)
    return answer


print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
