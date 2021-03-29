# 반복문자 지우기
# D2

import sys
sys.stdin = open('input_4873.txt')
T = int(input())
for test_case in range(1, T+1):
    input_str = list(map(str, input()))

    stack = []

    for i in range(len(input_str)):
        stack.append(input_str[i])
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    print('#{} {}'.format(test_case, len(stack)))
