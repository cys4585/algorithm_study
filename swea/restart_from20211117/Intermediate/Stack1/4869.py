import sys
sys.stdin = open('./4869_sample_input.txt', 'r')

def my_func(N):
    if N == 10: return 1
    elif N == 20: return 3
    else:
        return my_func(N-10) + 2*my_func(N-20)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = my_func(N)
    print(f'#{tc} {result}')