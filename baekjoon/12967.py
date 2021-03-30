# pqr

# N개의 수로 이루어진 배열 A, 정수 K
# 0 <= p < q < r < N
# (A[p] * A[q] * A[r]) % K == 0

# 위 조건을 만족하는 (p, q, r) 쌍의 개수 구하기


def function(start_idx, end_idx, arr, num, pqr):
    global cnt
    # print(start_idx, end_idx, num, pqr)
    if pqr == 3:
        if num % K == 0:
            cnt += 1
        return
    for i in range(start_idx, end_idx + 1):
        if not used[i]:
            used[i] = 1
            # print(i + 1, end_idx + 1, '/', i, num*arr[i], pqr + 1)
            function(i + 1, end_idx + 1, arr, num * arr[i], pqr + 1)
            used[i] = 0


N, K = map(int, input().split())
in_arr = list(map(int, input().split()))
cnt = 0
used = [0] * N
# function(0, N - 3, in_arr, 1, 0)
num = 1
for p in range(len(in_arr) - 2):
    num *= in_arr[p]
    for q in range(p + 1, len(in_arr) - 1):
        for r in range(q + 1, len(in_arr)):
            if (in_arr[p] * in_arr[q] * in_arr[r]) % K == 0:
                cnt += 1
    num //= in_arr[p]
print(cnt)
