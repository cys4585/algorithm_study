# 서비스 센터

# 싸피 전자는 V개의 지역을 담당하는 서비스센터를 새로 만들려고 한다.
# 이때 최적의 위치는 각 지역으로 부터의 이동 시간의 합이 최소가 되는 곳

# 각 지역을 연결하는 E개의 도로와 각 도로를 통한 이동 시간이 주어질 때
# 이동 시간의 합 중 최소인 값을 출력하는 프로그램을 만드시오.
# (지역마다 이름이 있지만 편의상 1번부터 V번으로 사용한다.)

# 첫 줄에는 테스트 케이스의 개수
# 다음 줄부터는 도시의 수 V, 도로의 수 E,
# E개읠 줄에 걸쳐 도로의 정보가 주어짐

# 4 <= V <= 100
# V-1 <= E <= V*(V-1)/2

'''
input
3
4 5
1 2 4
1 3 1
1 4 4
2 4 4
3 4 1
5 8
1 2 4
1 3 21
1 5 8
2 3 16
2 4 6
2 5 31
3 4 10
4 5 5
6 10
1 2 6
1 3 1
1 4 5
2 3 5
2 5 3
3 4 5
3 5 6
3 6 4
4 6 2
5 6 6
'''

'''
output
#1 7
#2 31
#3 21
'''


import sys
sys.stdin = open('문제3_input.txt')


def my_func(start):
    global result
    U = {start} # 선택된 노드
    D = A[start]  # 거리
    D[start] = 0

    while len(U) < V:
        # 선택되지 않은 노드 중에서 가장 가까운 노드 찾기
        min_d = INF
        min_idx = None
        for i in range(1, V+1):
            if i in U: continue
            if min_d > D[i]:
                min_d = D[i]
                min_idx = i
        # 가장 가까운 노드를 U에 추가
        U.add(min_idx)

        # D 갱신
        for i in range(1, V+1):
            if i in U: continue
            D[i] = min(D[i], D[min_idx] + A[min_idx][i])

    sum_v = sum(D[1:])
    if result > sum_v:
        result = sum_v
    # print(sum_v, result)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    INF = 0xffffff
    A = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        A[u][v] = w
        A[v][u] = w

    result = INF
    for i in range(1, V+1):
        my_func(i)
    # print()

    print(f'#{tc} {result}')