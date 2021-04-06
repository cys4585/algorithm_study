# 이진 탐색

# 1부터 N 까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
# 이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브 트리의 루트인 규칙을 만족한다.
# 추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들 수 있다.

# 완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
# N 이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과,
# N/2번 노드(N 이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('input_5176.txt')


def make_tree(v):
    global value
    # 범위 안에서만 탐색
    if v <= N:
        # left_child 방문
        make_tree(2 * v)
        # current node 에 value 넣기
        tree[v] = value
        value += 1
        # right_child 방문
        make_tree(2 * v + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    value = 1

    make_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))