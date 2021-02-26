# Forth
# D2
import sys
sys.stdin = open('input_4874.txt')
for test_case in range(1, int(input())+1):
    in_arr = input().split()

    stack = []
    operator = ['*', '/', '+', '-']

    for char in in_arr:
        if char in operator:
            if len(stack) < 2:
                print('#{} {}'.format(test_case, 'error'))
                break
            n1 = stack.pop(-2)
            n2 = stack.pop(-1)
            if char == '*':
                stack.append(n1 * n2)
            elif char == '/':
                stack.append(n1 // n2)
            elif char == '+':
                stack.append(n1 + n2)
            else:
                stack.append(n1 - n2)
        elif char == '.':
            if len(stack) != 1:
                print('#{} {}'.format(test_case, 'error'))
                break
            print('#{} {}'.format(test_case, stack.pop()))
        else:
            stack.append(int(char))
