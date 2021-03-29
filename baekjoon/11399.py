# ATM

N = int(input())
P_arr = list(map(int, input().split()))

# 오름차순으로 정렬하고 숫자를 더함

for _ in range(N-1):
    for j in range(N-1):
        if P_arr[j] > P_arr[j+1]: P_arr[j], P_arr[j+1] = P_arr[j+1], P_arr[j]
# print(P_arr)

sum_v = 0
for i in range(N):
    for j in range(0, i+1):
        sum_v += P_arr[j]
print(sum_v)
