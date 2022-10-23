input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []

    for spilt_size in range(1, n // 2 + 1):
        compressed = ""
        splited = [
            string[i:i + spilt_size] for i in range(0, n, spilt_size)
        ]
        count = 1  # 공통인 문자열 개수를 세는 변수

        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]  # 연속된 공통 문자열을 각각 변수 prev, cur에 저장한다.

            if prev == cur:
                count += 1  # 압축할 문자열 개수를 센다.
            else:  # 해당 문자열을 더 이상 압축할 수 없을 때,
                if count > 1:  # 해당 문자열을 압축한 적이 있는 경우
                    compressed += (str(count) + prev)  # 압축 길이와 압축한 문자열을 이어 붙인 문자열을 compressed에 저장한다.
                else:  # 해당 문자열을 압축한 적이 없는 경우
                    compressed += prev  # 압축하지 않은 문자열을 compressed에 이어 붙인다.
                count = 1  # count를 초기화한다.
        if count > 1:  # 반복을 끝내고 남은 cur를 compressed에 붙인다.
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
        compression_length_array.append(len(compressed))

    return min(compression_length_array)

print(string_compression(input))

# 예) 문자열을 길이 3으로 자를 경우 :
# ["abc, "abc", "abc", "abc", "ded", "ede", "ded", "ede"]
#   j == 1  ->  prev, cur = "abc", "abc"
#       prev == cur ->  count == 2
#   j == 2 ~ 3  ->  prev, cur = "abc", "abc"
#       prev == cur ->  count == 3 ~ 4
#   j == 4  ->  prev, cur = "abc", "ded"
#       prev != cur ->  count == 4 > 1  ->  compressed == 4abc, count = 1
#   j == 5  ->  prev, cur = "ded", "ede"
#       prev != cur ->  count == 1  ->  compressed == 4abc + ded, count = 1
#   j == 6  ->  prev, cur = "ede", "ded"
#       prev != cur ->  count == 1  ->  compressed == 4abcded + ede, count = 1
#   j == 7  ->  prev, cur = "ded", "ede"
#       prev != cur ->  count == 1  ->  compressed == 4abcdedede + ded, count = 1

# count == 1    ->  compressed = 4abcdedededed+ede == 4abcdededededede
