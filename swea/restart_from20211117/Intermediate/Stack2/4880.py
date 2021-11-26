import sys
sys.stdin = open('./4880_sample_input.txt', 'r')

def my_func(cards, i, j):
    if i == j: return i
    center = (i + j) // 2
    left = my_func(cards, i, center)
    right = my_func(cards, center + 1, j)
    if cards[left] == 1:
        if cards[right] == 2: return right
        else: return left
    elif cards[left] == 2:
        if cards[right] == 3: return right
        else: return left
    else:
        if cards[right] == 1: return right
        else: return left



for tc in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    result = my_func(cards, 0, N - 1)
    print(f'#{tc} {result + 1}')
