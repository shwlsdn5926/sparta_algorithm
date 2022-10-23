input = "반복하"


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        string = string[1:-1]
        return is_palindrome(string)
    return False


print(is_palindrome(input))

