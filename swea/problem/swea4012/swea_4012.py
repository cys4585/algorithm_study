# 요리사
# 난이도 ?
import sys
sys.stdin = open('input_4012.txt')

def synergy(arr):
    taste = 0
    for i in arr:
        for j in arr:
            taste += table[i][j]
    return taste

def choice(idx, cnt):
    global result
    if cnt == N//2:
        A, B = [], []
        for i in range(N):
            if used[i]: A.append(i)
            else: B.append(i)
        taste_A = synergy(A)
        taste_B = synergy(B)
        difference = abs(taste_A - taste_B)
        if result is None or difference < result: result = difference
        return
    for i in range(idx, N):
        if not used[i]:
            used[i] = 1
            choice(i, cnt + 1)
            used[i] = 0

for tc in range(1, int(input()) + 1):
    # N * N
    # 식재료들을 각각 N/2 개씩 나누어 두 개의 요리를 한다.
    # 각각의 음식 -> A, B
    # A와 B의 맛의 차이가 최소가 되도록 재료를 배분하기
    # 식재료의 조합(시너지 값)에 따라 음식의 맛 결정됨
    # 각 음식의 맛은 식재료의 시너지 값들의 합

    # 두 음식 간의 맛의 차이(시너지의 합의 차)가 최소가 될 때의 최솟값 출력

    N = int(input())    # N개의 식재료 (짝수)
    table = [list(map(int, input().split())) for _ in range(N)]
    # print(N, table)

    used = [0] * N
    result = None
    choice(0, 0)
    print('#{} {}'.format(tc, result))
