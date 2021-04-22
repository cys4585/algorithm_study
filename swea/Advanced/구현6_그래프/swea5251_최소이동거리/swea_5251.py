# 최소 이동 거리 (D4)

# A도시에는 E개의 일방통행 도로 구간이 있으며,
# 각 구간이 만나는 연결지점에는 0번부터 N번까지의 번호가 붙어있다.

# 구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때,
# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.

# 모든 연결 지점을 거쳐가야 하는 것은 아니다.

import sys
sys.stdin = open('input_5251.txt')


def my_func(start):
    weight = [0xffffff] * (N+1)
    weight[0] = 0
    selected = [0]

    while N not in selected:
        min_w = 0xffffff
        min_idx = None

        for v in selected:
            for i in range(N+1):
                if adj[v][i] == 0: continue
                if i in selected: continue
                if weight[i] > weight[v] + adj[v][i]:
                    weight[i] = weight[v] + adj[v][i]
                # print(v, i, min_w, weight[i], adj[v][i])
                if min_w > weight[i]:
                    min_w = weight[i]
                    min_idx = i

        selected.append(min_idx)
        # print(selected, weight)
    return weight[-1]




for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    INF = 0xffffff
    adj = [[0] * (N+1) for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    print('#{} {}'.format(tc, my_func(0)))