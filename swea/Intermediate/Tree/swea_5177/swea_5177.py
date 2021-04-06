# 이진 힙

# 이진 최소힙은 다음과 같은 특징을 가진다.
#   - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
#   - (부모 노드의 값 < 자식 노드의 값)을 유지한다.
#   - 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
#   - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.

import sys
sys.stdin = open('input_5177.txt')


def swap_node(child):
    parent = child // 2
    # parent node 값이 child node 값보다 크면
    if tree[parent] > tree[child]:
        # node 위치를 바꿔준다.
        tree[parent], tree[child] = tree[child], tree[parent]
        # 자리를 교체한 parent node와 그 위의 node(parent의 parent)와 비교
        swap_node(parent)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    in_arr = list(map(int, input().split()))

    tree = [0]
    node = 0    # 정점 번호
    for value in in_arr:
        node += 1
        tree.append(value)  # Tree 에 Node 추가
        if len(tree) == 1: continue     # Root Node 만들 때는 작업 X
        swap_node(node)     # current node, parent node 비교하여 자리 바꾸기

    # 마지막 node의 조상 노드의 값 모두 더하기
    sum_node = N
    sum_v = 0
    while sum_node > 1:
        sum_node //= 2
        sum_v += tree[sum_node]

    print('#{} {}'.format(tc, sum_v))

