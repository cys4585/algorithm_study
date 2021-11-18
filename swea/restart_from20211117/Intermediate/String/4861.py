import sys
sys.stdin = open('./4861_sample_input.txt', 'r')

def my_func(string):
    for i in range(N - M + 1):
        sub_str = string[i:i+M]
        for j in range(M // 2):
             if sub_str[j] != sub_str[-(1+j)]:
                break
        else:
            return sub_str
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    board = [input() for _ in range(N)]
    # print(N, M)
    # for i in range(N): print(board[i])

    for i in range(N):
        hor_str = board[i]
        ver_str = ''
        for j in range(N):
            ver_str += board[j][i]
        hor_result = my_func(hor_str)
        ver_result = my_func(ver_str)
        if hor_result:
            result = hor_result
            break
        elif ver_result:
            result = ver_result
            break

    print(f'#{tc} {result}')