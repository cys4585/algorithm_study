import sys
sys.stdin = open('./4874_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    in_lst = input().split()

    stack = []
    result = None
    for c in in_lst:
        if c in '+-*/':
            if len(stack) < 2:
                result = 'error'
                break
            n2, n1 = stack.pop(), stack.pop()
            if c == '+': stack.append(n1 + n2)
            elif c == '-': stack.append(n1 - n2)
            elif c == '*': stack.append(n1 * n2)
            elif c == '/': stack.append(n1 // n2)
        elif c == '.':
            if len(stack) != 1:
                result = 'error'
                break
            result = stack.pop()
        else:
            stack.append(int(c))

    print(f'#{tc} {result}')