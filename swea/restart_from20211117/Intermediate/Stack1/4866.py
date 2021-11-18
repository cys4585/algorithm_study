import sys
sys.stdin = open('./4866_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    in_str = input()
    stack = []

    result = True
    for c in in_str:
        if c == '{' or c == '(':
            stack.append(c)
        elif c == '}' or c == ')':
            if len(stack) == 0:
                result = False
                break
            fair = stack.pop()
            if fair != '{' and c == '}':
                result = False
                break
            elif fair != '(' and c == ')':
                result = False
                break
    else:
        if len(stack) != 0: result = False

    print(f'#{tc} {int(result)}')