# 쉬운 거스름돈

# S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면
# 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.

# 10 <= N <= 1,000,000
# N의 마지막 자릿수는 항상 0

import sys
sys.stdin = open('input_1970.txt')

cashes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, int(input()) + 1):
    change = int(input())

    cnt = list()
    for cash in cashes:
        cnt.append(change // cash)
        change %= cash

    print(f'#{tc}')
    for c in cnt:
        print(c, end=' ')
    print()