import sys

sys.stdin = open("input_4839_binary_search.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    Al = 1
    Ar = P
    Bl = 1
    Br = P

    winner = '0'

    while True:
        Ac = (Ar + Al) // 2
        Bc = (Br + Bl) // 2

        if Ac == A:
            if not Bc == B:
                winner = 'A'
            break
        elif Bc == B:
            if not Ac == A:
                winner = 'B'
            break
        else:
            if Ac < A:
                Al = Ac
            elif Ac > A:
                Ar = Ac
            if Bc < B:
                Bl = Bc
            elif Bc > B:
                Br = Bc

    print('#{} {}'.format(test_case, winner))