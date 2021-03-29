import sys
sys.stdin = open("input_4865_number_of_characters.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = {}
    for c in str1:
        result[c] = 0

    for k in result.keys():
        for c in str2:
            if k == c:
                result[k] += 1

    max_v = 0
    for v in result.values():
        if max_v < v:
            max_v = v

    print('#{} {}'.format(test_case, max_v))