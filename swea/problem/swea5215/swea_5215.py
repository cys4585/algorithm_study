# 햄버거 다이어트
# D3
import sys
sys.stdin = open("input_5215.txt")

def function(n, score, kcal):
    global max_score
    if kcal > L:
        return "over"
    if max_score < score: max_score = score
    for i in range(n, N):
        if not used[i]:
            used[i] = 1
            if function(i, score + evaluation_table[i][0], kcal + evaluation_table[i][1]) == "over":
                if max_score < score: max_score = score
            used[i] = 0

for tc in range(1, int(input()) + 1):
    # N : 재료의 수
    # L : 제한 칼로리
    N, L = map(int, input().split())
    # evaluation_table : [점수, 칼로리]
    evaluation_table = [list(map(int, input().split())) for _ in range(N)]
    print(N, L, evaluation_table)

    max_score = 0       # 맛의 점수를 합할 변수
    used = [0] * N  # 재료 사용 유무 체크

    function(0, 0, 0)
    print("#{} {}".format(tc, max_score))