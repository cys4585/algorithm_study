# 중위순회 (in-order traversal)

# 총 노드의 개수는 100개 이하
# 트리는 완전 트리 형식으로 주어짐
# 노드당 하나의 알파벳만 저장
# 노드가 주어지는 순서는 숫자 번호대로 주어짐 (1부터 ...)

# 첫 줄에는 트리가 갖는 정점의 총 수 N(1 <= N <= 100)이 주어짐
# 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어짐

# 정점번호는 1부터 N까지의 정수로 구분
# 루트 정점의 번호는 반드시 1

# 입력에서 이웃한 알파벳이나 자식 정점의 번호는 모두 공백으로 구분

import sys
sys.stdin = open('input_1231.txt', 'r')


def in_order_traversal(v):
    if node[v]:     # 노드의 value 존재하면
        in_order_traversal(left[v])     # left_child 방문
        print(node[v], end='')          # current node 의 value 출력
        in_order_traversal(right[v])    # right_child 방문

T = 10
for tc in range(1, T + 1):
    N = int(input())
    in_arr = [input().split() for _ in range(N)]

    root = 1                # root 는 항상 1
    node = [0] * (N + 1)    # node 의 value
    left = [0] * (N + 1)    # 왼쪽자식 node 번호
    right = [0] * (N + 1)   # 오른쪽자식 node 번호

    for arr in in_arr:
        # [노드번호, value, left_child, right_child]
        # ex) ['1', 'W', '2', '3']
        idx = int(arr[0])
        node[idx] = arr[1]  # 노드번호에 맞는 value 저장
        if len(arr) >= 3:
            left[idx] = int(arr[2])     # 노드번호에 맞는 left_child 저장
            if len(arr) == 4:
                right[idx] = int(arr[3])    # 노드 번호에 맞는 right_child 저장

    print('#{}'.format(tc), end=' ')
    in_order_traversal(root)
    print()