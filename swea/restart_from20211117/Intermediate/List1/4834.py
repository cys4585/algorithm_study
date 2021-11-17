import sys
sys.stdin = open("./4834_sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    cnt_list = [0] * 10
    for i in cards:
        cnt_list[i] += 1

    max_n, max_c = 0, 0
    for num, cnt in enumerate(cnt_list):
        if max_c <= cnt:
            max_c = cnt
            max_n = num
    print(f'#{tc} {max_n} {max_c}')
