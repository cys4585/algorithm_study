# 노드의 합

# 완전 이진 트리(Complete Binary Tree)의 리프 노드(leaf node)에 1000 이하의 자연수가 저장되어 있고,
# 리프 노드를 제외한 노드에는 자식 노드(child node)에 저장된 값의 합이 들어있다고 한다.

# N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며,
# 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.

# 완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.

# 리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음,
# 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성하시오.

import sys
sys.stdin = open('input_5178.txt')

T = int(input())
for tc in range(1, T + 1):
    # N : 노드의 개수
    # M : 리프 노드의 개수
    # L : 출력할 노드 번호
    N, M, L = map(int, input().split())
    # (리프 노드 번호, 값)
    in_arr = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)
    for i, val in in_arr:
        tree[i] = val

    for i in range(N - M, 0, -1):
        left_child, right_child = 2 * i, 2 * i + 1
        parent_val = tree[left_child]
        if right_child <= N:
            parent_val += tree[right_child]
        tree[i] = parent_val

    print('#{} {}'.format(tc, tree[L]))