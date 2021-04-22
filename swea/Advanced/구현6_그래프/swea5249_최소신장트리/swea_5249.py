# 최소 신장 트리 (D4)

# 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
# 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
# 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('input_5249.txt')

# x의 대표자(representative) 리턴
def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])

# y의 대표자를 x로 바꾸기
def union(x, y):
    representative_of_x = find_set(x)
    representative_of_y = find_set(y)
    if representative_of_x == representative_of_y:
        return
    parent[representative_of_y] = representative_of_x


def kruskal():
    data.sort(key=lambda x: x[2])

    result = 0
    for i in range(E):
        v1, v2, w = data[i]
        # v1과 v2의 대표자가 같으면 -> 패스
        # v1과 v2의 대표자가 같은데 v1과 v2를 합치면 사이클 경로가 됨
        if find_set(v1) == find_set(v2): continue
        union(v1, v2)
        result += w
    return result



for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    INF = 0xffffff
    data = list()
    for i in range(E):
        n1, n2, w = map(int, input().split())
        data.append((n1, n2, w))

    parent = [i for i in range(V+1)]

    print(f'#{tc} {kruskal()}')
