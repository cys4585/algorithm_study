import sys
sys.stdin = open('./5097_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        numbers.append(numbers.pop(0))

    print(f'#{tc} {numbers[0]}')