def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if i.isalpha():
            alphabet_occurrence_array[ord(i) - ord('a')] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))

# 내장 함수 ord() 이용해서 아스키 값 받기

# 질문
# 1. 문자열을 어떻게 알파벳에 대응시킬까?
# 2. 스페이스를 알파벳으로 인식하지 않게 하려면 어떻게 할까?
# 3. 알파벳 배열 순서를 어떻게 알 수 있을까?
# 4. 알파벳의 수를 어떻게 알 수 있을까?
# 1) 알파벳 개수를 저장한 리스트를 만든다.
# list[0]= ord('b') - ord('a')
# 2) 리스트에서 최댓값에 해당하는 인덱스를 구한다.
# 3) 인덱스에 대응되는 알파벳을 반환한다.
