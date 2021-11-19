import sys
sys.stdin = open('./4871_sample_input.txt', 'r')

def my_func(edges, s_node, goal):
    global result
    if s_node == goal: result = 1
    for s, g in edges:
        if s == s_node:
            my_func(edges, g, goal)

for tc in range(1, int(input()) + 1):
    V, E = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    result = 0
    my_func(edges, S, G)
    print(f'#{tc} {result}')