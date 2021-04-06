# subtree
# D2

# 주어진 이진 트리(Binary Tree)에서 노드 N을 루트로 하는 서브 트리(sub tree)에 속한
# 노드의 개수를 알아내는 프로그램

# 주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없다.
# 부모가 없는 노드가 전체의 루트 노드가 된다.

import sys
sys.stdin = open('input_5174.txt')


def find_node(v):
    global cnt
    cnt += 1
    if left[v]: find_node(left[v])
    if right[v]: find_node(right[v])


for tc in range(1, int(input()) + 1):
    E, sub_root = map(int, input().split())
    in_arr = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)
    for i in range(0, len(in_arr), 2):
        parent, child = in_arr[i], in_arr[i + 1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    cnt = 0
    find_node(sub_root)
    print('#{} {}'.format(tc, cnt))