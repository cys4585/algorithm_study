# 계산기3
# D4
import sys
sys.stdin = open('input_1224.txt')
for tc in range(1, 11):
    len_of_tc = int(input())
    in_arr = list(map(str, input()))
    # print(in_arr)

    operator = ['(', '*', '+', ')']
    change_arr = list()
    operator_stack = list()
    for c in in_arr:
        if c in operator:
            if c == '(':
                operator_stack.append(c)
            elif c == '+':
                if not operator_stack:
                    operator_stack.append(c)
                elif operator_stack[-1] == '(':
                    operator_stack.append(c)
                else:
                    change_arr.append(operator_stack.pop())
                    operator_stack.append(c)
            elif c == '*':
                if not operator_stack:
                    operator_stack.append(c)
                elif operator_stack[-1] == '(':
                    operator_stack.append(c)
                elif operator_stack[-1] == '+':
                    operator_stack.append(c)
                else:
                    change_arr.append(operator_stack.pop())
                    operator_stack.append(c)
            elif c == ')':
                while operator_stack[-1] != '(':
                    change_arr.append(operator_stack.pop())
                operator_stack.pop()    # '(' 지우기
        else:
            change_arr.append(c)

    while operator_stack:
        change_arr.append(operator_stack.pop())

    # print(change_arr)
    stack = list()
    for char in change_arr:
        # print(stack, char)
        if char in operator:
            num1, num2 = int(stack.pop(-2)), int(stack.pop(-1))
            if char == '*':
                stack.append(num1 * num2)
            elif char == '+':
                stack.append(num1 + num2)
        else:
            stack.append(int(char))

    print('#{} {}'.format(tc, stack.pop()))