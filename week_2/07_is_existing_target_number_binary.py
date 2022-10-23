finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    cur_min = 0
    cur_max = len(numbers) - 1
    crit = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if numbers[crit] == target:
            return True
        elif numbers[crit] < target:
            cur_min = crit + 1
        else:
            cur_max = crit - 1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
