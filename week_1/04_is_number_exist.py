input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for i in array:
        if i == number:
            return True

    return False

result = is_number_exist(0, input)
print(result)