import sys
sys.stdin = open("input_4866_bracket_check.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()

    bracket_stack = []

    result = 0
    for c in string:
        if c == '(' or c == '{' or c == '[':
            bracket_stack.append(c)
        elif c == ')' or c == '}' or c == ']':
            if len(bracket_stack) == 0: break
            pop_c = bracket_stack.pop()
            if (c == ')' and pop_c != '(') or (c == '}' and pop_c != '{') or (c == ']' and pop_c != '['):
                break
    else:
        if len(bracket_stack) == 0:
            result = 1

    print('#{} {}'.format(test_case, result))