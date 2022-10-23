# 문자열을 공백으로 줄 때, 왜 'a'를 반환할까? -> max_alphabet의 값이 업데이트가 안 되기 때문이다.
# max_occurence의 값이 0으로 일정하므로 if 조건문을 실행하지 못한다.

input = ""


# 알파벳 리스트를 만들어 빈도수가 가장 높은 알파벳 찾기


# 각 알파벳에 대해 빈도수를 구해야 한다 -> for 알파벳 in 알파벳 배열
#     '문자열'을 이루는 각 문자 i와 같은 알파벳의 개수를 빈도수로 구한다.-> 빈도수 =0, for i in 문자열
#         '행동 B' : i==알파벳 -> 빈도수 증가


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]

    max_occurence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurence = 0
        for i in string:
            if i == alphabet:
                occurence += 1
        if occurence > max_occurence:
            # 빈도수 업데이트하는 동시에 대응되는 알파벳을 업데이트한다.
            max_alphabet = alphabet
            max_occurence = occurence

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)
