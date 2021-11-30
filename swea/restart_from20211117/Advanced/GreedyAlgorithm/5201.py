import sys
sys.stdin = open('./5201_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    total_weight = 0
    while trucks:
        truck = trucks.pop(0)
        while containers:
            container = containers.pop(0)
            if container <= truck:
                total_weight += container
                break

    print(f'#{tc} {total_weight}')
