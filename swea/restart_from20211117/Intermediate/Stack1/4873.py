import sys
sys.stdin = open('./4873_sample_input.txt', 'r')

def my_func(in_list):
    stack = []
    for c in in_list:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    return len(stack)

for tc in range(1, int(input()) + 1):
    in_str = input()

    result = my_func(list(in_str))
    print(f'#{tc} {result}')
