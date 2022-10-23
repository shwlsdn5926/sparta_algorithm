s = "((())"


def is_correct_parenthesis(string):
    n = len(string)

    if string[0] == "(" and string[n - 1] == ")":
        parent_check = ["("]
        for i in range(1, n):
            if string[i] == "(":
                parent_check.append("(")
            else:
                if not parent_check:
                    return False
                parent_check.pop()
        if not parent_check:
            return True

    return False


print(is_correct_parenthesis(s))
