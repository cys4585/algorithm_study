# 그룹 나누기 (D3)

# 수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

# 한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나
# 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

# 예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면,
# 1-2-3번이 같은 조가 된다.
# 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

# 1번부터 N번까지의 출석번호가 있고, M장의 신청서가 제출되었을 때
# 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('input_5248.txt')

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x, y):
    representative_of_x = find_set(x)
    representative_of_y = find_set(y)

    if representative_of_x == representative_of_y:
        return
    parent[representative_of_y] = representative_of_x


for tc in range(1, int(input()) + 1):
    # N : 사람 번호 (2 <= N <= 100)
    # M : 신청서 수 (1 <= M <= 100)
    N, M = map(int, input().split())
    in_arr = list(map(int, input().split()))

    parent = [0]
    for i in range(1, N+1):
        parent.append(i)

    for i in range(M):
        a, b = in_arr[i*2], in_arr[i*2+1]
        union(a, b)

    representative = set()
    for i in range(1, N+1):
        representative.add(find_set(i))

    print(f'#{tc} {len(representative)}')
