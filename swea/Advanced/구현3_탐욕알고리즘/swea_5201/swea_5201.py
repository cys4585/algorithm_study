# 컨테이너 운반

# 화물이 실려있는 N개의 컨테이너를 M대의 트럭으로 A -> B 도시로 운반하려고 한다.

# 트렁당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고,
# A도시에서 B도시로 최대 M대의 트럭이 편도로 한번만 운행된다고 한다.

# 이 때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면,
# 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다.
# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

import sys
sys.stdin = open('input_5201.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    trucks.sort(reverse=True)
    containers.sort(reverse=True)

    sum_v = 0
    checked = [0] * N
    for i in range(M):
        for j in range(i, N):
            if checked[j]: continue
            if trucks[i] >= containers[j]:
                checked[j] = 1
                sum_v += containers[j]
                break

    print(f'#{tc} {sum_v}')