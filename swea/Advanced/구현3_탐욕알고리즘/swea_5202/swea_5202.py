# 화물 도크

# 화물을 싣고 내리는 도크

# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
# 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
# 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

import sys
sys.stdin = open('input_5202.txt')


def function(idx, cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    if idx == N:
        return

    for i in range(idx, N):
        start, end = start_end[i]
        if 1 in time[start:end]:
            continue
        for t in range(start, end):
            time[t] = 1
        function(i + 1, cnt + 1)
        for t in range(start, end):
            time[t] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    start_end = [list(map(int, input().split())) for _ in range(N)]

    time = [0] * 25     # 0시 ~ 24시
    checked = [0] * N   # 작업 가능한 화물 체크
    max_cnt = 0

    print(N)
    print(start_end)
    function(0, 0)

    print(f'#{tc} {max_cnt}')