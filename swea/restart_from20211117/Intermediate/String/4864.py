import sys
sys.stdin = open('./4864_sample_input.txt', 'r')

def my_func(str1, str2, idx1, idx2):
    if idx1 >= len(str1):
        return 1
    for i in range(idx2, len(str2)):
        if str1[idx1] == str2[i]:
            return my_func(str1, str2, idx1+1, i + 1)
    return 0

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = my_func(str1, str2, 0, 0)
    print(f'#{tc} {result}')