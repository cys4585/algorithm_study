# 스타트와 링크

# 축구는 평일 오후에 하고 의무 참석도 아니다.
# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
# 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

# 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
# 능력치 S[i][j]는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 S[i][j]의 합이다.
# S[i][j]는 S[j][i]와 다를 수도 있으며,
# i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S[i][j]와 S[j][i]이다.

# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.


def sub_func(team1):
    global min_sub_v

    team2 = []
    for i in range(N):
        if i not in team1:
            team2.append(i)

    stat1 = stat2 = 0
    for i in range(N // 2 - 1):
        i_t1 = team1[i]
        i_t2 = team2[i]
        for j in range(i + 1, N // 2):
            j_t1 = team1[j]
            j_t2 = team2[j]
            stat1 += (S[i_t1][j_t1] + S[j_t1][i_t1])
            stat2 += (S[i_t2][j_t2] + S[j_t2][i_t2])

    sub_v = abs(stat1 - stat2)
    if min_sub_v > sub_v:
        min_sub_v = sub_v


def brute_force(idx, team1):
    if len(team1) == N // 2:
        return sub_func(team1)

    for i in range(idx + 1, N):
        if used[i]: continue
        used[i] = 1
        brute_force(i, team1 + [i])
        used[i] = 0


# 4 <= N <= 20, N은 짝수
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_sub_v = 0xffffff
used = [0] * N
brute_force(-1, [])

print(min_sub_v)