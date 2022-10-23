finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    crit = (cur_min + cur_max) // 2
    # find_count = 0

    while cur_min <= cur_max:
        # find_count += 1
        if array[crit] == target:
            # print(find_count) # 14!
            return True
        elif array[crit] < target:
            cur_min = crit + 1
        else:
            cur_max = crit - 1
        crit = (cur_min + cur_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
