# 보이어-무어 알고리즘
# 문자열 찾기
import sys
sys.stdin = open('input_4864.txt')

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = False

    jump = 0

    while jump + len(str1) <= len(str2):
        for i in range(len(str1) - 1, -1, -1):
            # 문자가 같으면
            if str1[i] == str2[jump + i]:
                continue
            # 문자가 하나라도 다르면
            else:
                # i == 3
                # str2[jump + i] == f
                for j in range(len(str1) - 1, -1, -1):
                    if str2[jump + i] == str1[j]:
                        jump = (jump + i) - j
                        break
                else:
                    jump += len(str1)
                break
        # 문자가 모두 같으면(break가 실행되지 않았으면)
        else:
            result = True
            break

    print('#{} {}'.format(test_case, int(result)))