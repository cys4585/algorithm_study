# 토너먼트 카드게임
# D2

# 못풀어서 웹에서 힌트를 얻고 품...
# 재귀함수에 대한 이해가 필요할 듯 하다.
# 재귀를 여러번 하는 거라면 -> 함수가 쌓이는 스택에 대한 공부라고 생각해야 하나..?
import sys
sys.stdin = open('input_4880.txt')

def rock_scisor_paper(i, j):
    a, b = in_arr[i - 1], in_arr[j - 1]
    if a == b: return i
    else:
        if a == '1':
            if b == '2': return j
            elif b == '3': return i
        if a == '2':
            if b == '3': return j
            elif b == '1': return i
        if a == '3':
            if b == '1': return j
            elif b == '2': return i

def group_split(i, j):
    if i == j: return i
    center = (i + j) // 2
    winner_group_1 = group_split(i, center)
    winner_group_2 = group_split(center+1, j)
    return rock_scisor_paper(winner_group_1, winner_group_2)

for test_case in range(1, int(input())+1):
    N = int(input())    # 전체 인원
    in_arr = input().split()

    i = 1
    j = N
    result = group_split(i, j)
    print('#{} {}'.format(test_case, result))