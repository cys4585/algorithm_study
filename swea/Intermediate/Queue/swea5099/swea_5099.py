# 피자 굽기
# D3
import sys
sys.stdin = open('input_5099.txt')

def function(pizzas_arr):
    oven_queue = list()
    for _ in range(N):
        oven_queue.append(pizzas_arr.pop(0))
    # print(queue, pizzas)
    while len(oven_queue) > 1:
        pizza = oven_queue.pop(0)
        pizza[0] //= 2  # 치즈 녹이기
        if pizza[0] > 0: oven_queue.append(pizza)
        elif pizzas_arr: oven_queue.append(pizzas_arr.pop(0))
    return oven_queue[0][1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    in_arr = list(map(int, input().split()))
    # print(tc, N, M, in_arr)

    for i in range(M):
        in_arr.append([in_arr.pop(0), i + 1])   # 피자의 번호를 추가 (식별을 위해)
    # print(in_arr)

    print('#{} {}'.format(tc, function(in_arr)))