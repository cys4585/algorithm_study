# 차이를 최대로

# N개의 정수로 이루어진 배열 A가 주어진다.
# 이 때, 배열에 들어있는 정수의 순서를 적절히 바꿔서
# 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0]-A[1]| + |A[1]-A[2]| + ... + |A[N-2]-A[N-1]|


# 두 수의 차의 절대값 계산에서
# 뒤에있는 값이 다음 계산에서는 앞으로 와야한다. (꼬리물기처럼)
# 그래서 뒤의 값을 함수의 인자로 보내서
# 다음 계산에서 사용할 수 있도록 한다.
# i : 절대값 계산에서 앞에 올 값
def my_func(i, sum_v):
    global max_v
    if 0 not in used:
        if max_v < sum_v:
            max_v = sum_v
        return
    # 뒤에 올 값을 골라준다.
    for j in range(N):
        if used[j]: continue
        used[j] = 1
        # 뒤에 온 값이 다음 함수에서는 앞으로 간다.
        my_func(j, sum_v + abs(A[i] - A[j]))
        used[j] = 0


# 3 <= N <= 8
# 배열 A의 모든 원소 A[i]  -100 <= A[i] <= 100
N = int(input())
A = list(map(int, input().split()))

max_v = 0
used = [0] * N
for i in range(N):
    used[i] = 1
    my_func(i, 0)
    used[i] = 0
print(max_v)