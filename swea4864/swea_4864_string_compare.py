import sys

sys.stdin = open("input_4864_string_compare.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()   # 길이 : N
    str2 = input()   # 길이 : M

    # M - N + 1
    result = False
    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
        else:
            result = True
            break
    print('#{} {}'.format(test_case, int(result)))