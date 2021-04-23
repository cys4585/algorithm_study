# 창용 마을 무리의 개수 (D4)

# 창용 마을에는 N명의 사람이 살고 있다.

# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.

# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.

# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.

# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.

import sys
sys.stdin = open('input_7465.txt')

def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])


for tc in range(1, int(input()) + 1):
    # N : 창용 마을에 사는 사람의 수 (1 <= N <= 100)
    # M : 서로를 알고 있는 사람의 관계 수 (0 <= M <= N(N-1)/2)
    N, M = map(int, input().split())
    in_arr = [tuple(map(int, input().split())) for _ in range(M)]

    # parent : 각 idx의 부모 번호가 저장됨 (1번~N번)
    parent = [i for i in range(N+1)]

    for u, v in in_arr:
        parent[find_set(v)] = parent[find_set(u)]

    representative = set()
    for i in range(1, len(parent)):
        # 대표자의 부모는 자기 자신
        representative.add(parent[find_set(i)])

    print(f'#{tc} {len(representative)}')