input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if i.isalpha():
            alphabet_occurrence_array[ord(i) - ord('a')] += 1

    not_repeating_character_array = []

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + 97))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"

result = find_not_repeating_character(input)
print(result)
