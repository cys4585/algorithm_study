import sys
sys.stdin = open('./4828_sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 5 <= N <= 1000
    a_list = list(map(int, input().split()))    # 1 ,= ai <= 1000000

    min_a, max_a = a_list[0], a_list[0]
    for i in range(1, len(a_list)):
        if a_list[i] < min_a: min_a = a_list[i]
        if a_list[i] > max_a: max_a = a_list[i]

    result = max_a - min_a
    print(f'#{tc} {result}')
