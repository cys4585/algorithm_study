import sys

sys.stdin = open("input_6485_bus_route.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N : 버스 노선
    N = int(input())

    A_B_list = []
    for _ in range(N):
        A_B_list.append(list(map(int, input().split())))

    # P : 노선 수를 구해야 할 버스 정류장의 갯수
    P = int(input())

    C_list = []
    for _ in range(P):
        C_list.append(int(input()))

    result_list = [0] * P
    for a, b in A_B_list:
        for i, c in enumerate(C_list):
            if a <= c <= b:
                result_list[i] += 1

    print('#{}'.format(test_case), end=' ')
    for r in result_list:
        print(r, end=' ')
    print()