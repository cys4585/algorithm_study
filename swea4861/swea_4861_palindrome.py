import sys

sys.stdin = open("input_4861_palindrome.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    str_list = []

    for i in range(N):
        str_list.append(input())

    result = ''
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                # print(str_list[i][j+k], str_list[i][-(N-M+1-j+k)])
                if str_list[i][j+k] != str_list[i][-(N-M+1-j+k)]:
                    break
            else:
                result = str_list[i][j:j+M]
                break
            for k in range(M//2):
                if str_list[j + k][i] != str_list[-(N - M + 1 - j + k)][i]:
                    break
            else:
                for tmp_str in str_list[j:j + M]:
                    result += tmp_str[i]
                break
        if result != '':
            break

    print('#{} {}'.format(test_case, result))
