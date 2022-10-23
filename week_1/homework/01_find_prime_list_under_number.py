input = 10000


def find_prime_list_under_number(number):
    prime_array = []
    # 반복문을 이용하면 자연수를 순서대로 나열한 배열을 굳이 만들 필요 없다.
    for i in range(2, number + 1):
        # i가 j로 나누어떨어지지 않는다면 j를 소인수로 갖는 어떤 자연수라도 i를 나눌 수 없다.
        for j in prime_array:
            if i % j == 0 and j * j <= i:
                # 조건을 만족시키는 j가 하나라도 존재하면 반복을 중단한다.
                break
        # 조건을 만족시키는 j가 하나도 없으면 다음을 수행한다.
        else:
            prime_array.append(i)
    return prime_array


result = find_prime_list_under_number(input)
print(result)
