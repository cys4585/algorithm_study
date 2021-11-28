import sys
sys.stdin = open('./5099_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    oven = [None] * N
    oven_idx = 0

    pizza_idx = 0
    last_pizza = None
    while True:
        if oven[oven_idx]:
            pizza, pizza_num = oven[oven_idx]
            pizza //= 2
            if pizza == 0:
                last_pizza = pizza_num
                oven[oven_idx] = None
                for o in oven:
                    if o: break
                else: break
            else:
                oven[oven_idx] = (pizza, pizza_num)
        if not oven[oven_idx] and pizza_idx < M:
            pizza = pizzas[pizza_idx]
            pizza_idx += 1
            oven[oven_idx] = (pizza, pizza_idx)
        oven_idx += 1
        if oven_idx == N: oven_idx = 0

    print(f'#{tc} {last_pizza}')
