# 빈도수가 같은 문자가 존재하면 최빈값이 두 개 이상이 되어야 하지 않을까?
input = "best of best sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if i.isalpha():
            alphabet_occurrence_array[ord(i) - ord('a')] += 1
    # 최대 인덱스를 업데이트하기 위해 for문을 돌린다. 최대 빈도수를 업데이트하는 if 조건을 만족할 때 최대 인덱스를 업데이트한다.
    # for 인덱스 in 최대 인덱스 -> if 빈도수 > 최대 빈도수 -> 최대 빈도수 업데이트, 최대 인덱스 업데이트
    
    # 아래는 index()함수를 이용하여 index 변수를 만들지 않고, 빈도수 업데이트만으로 알파벳을 반환하는 코드
    max_num = alphabet_occurrence_array[0]
    for num in alphabet_occurrence_array:
        # 다음 조건에 해당하는 경우에만 max_num 값 변경
        if num > max_num:
            max_num = num
    # 반복이 모두 끝난 후 max_num 값 출력
    return chr(alphabet_occurrence_array.index(max_num) + 97)


result = find_max_occurred_alphabet(input)
print(result)
