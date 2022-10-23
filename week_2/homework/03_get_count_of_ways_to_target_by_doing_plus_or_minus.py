numbers = [1, 3, 1, 6]
target_number = 10
result_count = 0


def get_all_ways_to_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array):  # 탈출조건!
        if current_sum == target:
            global result_count
            result_count += 1  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + array[current_index])
    get_all_ways_to_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - array[current_index])


get_all_ways_to_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_count)

# 진심 소름돋는다.
# global 변수가 필요하다니... 재귀함수만 알아선 이 문제 못 풀겠구나.
# 함수를 병렬 호출하면 모든 경우의 수를 반환할 수 있다.

# 수학보다 코딩이 아름답다고 느끼기 시작했다.