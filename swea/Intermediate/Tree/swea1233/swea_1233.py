# 사칙연산 유효성 검사

# 사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다.
# 임의의 정점(node)에 연산자가 있으면 해당 연산자의 왼쪽 서브트리의 결과과 오른쪽 서브 트리의 결과를 사용해서 해당 연산자를 적용한다.

# 사칙연산 + - * / 와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때, 이 식의 유효성을 검사하는 프로그램을 작성하여라.
# 여기서 말하는 유효성이란, 사칙연산 + - * / 와 양의 정수로 구성된 임의의 식이 적절한 식인지를 확인하는 것으로,
# 계산이 가능하다면 1, 계산이 불가능할 경우 0을 출력
# (단, 0으로 나누는 경우는 고려하지 않는다.)

# 노드의 개수는 200개 이하
# 트리는 완전 이진 트리(Complete Binary Tree) 형식
# 노드당 하나의 연산자 또는 숫자만 저장할 수 있다.

import sys
sys.stdin = open('input_1233.txt')


def operate(v):
    # 현재 노드의 key가 연산자이면
    if tree[v] in operator:
        # 현재 노드가 자식이 없으면 유효하지 않는 식
        if not left_child[v] or not right_child[v]:
            return 'invalid'
        left_val = operate(left_child[v])
        right_val = operate(right_child[v])
        # 서브 트리가 유효하지 않는 식이라면 현재 트리도 유효하지 않음
        if left_val == 'invalid' or right_val == 'invalid':
            return 'invalid'
        if left_val == 'zero division error' or right_val == 'zero division error':
            return 'zero division error'
        # 연산작업 후 return
        result = 0
        if tree[v] == '+': result = left_val + right_val
        elif tree[v] == '-': result = left_val - right_val
        elif tree[v] == '*': result = left_val * right_val
        else:
            if right_val == 0:
                return 'zero division error'
            result = left_val / right_val
        return result
    # 현재 노드의 key가 정수이면
    else:
        # 현재 노드가 자식이 있으면 유효하지 않는 식
        if left_child[v] or right_child[v]:
            return 'invalid'
        # 자식이 없으면 현재 key(정수) 리턴
        return tree[v]


operator = ['+', '-', '*', '/']
for tc in range(1, 11):
    # 노드의 개수
    N = int(input())
    # 노드의 정보
    # [node, key, left child, right child]
    in_arr = [input().split() for _ in range(N)]

    tree = [0] * (N + 1)
    left_child = [0] * (N + 1)
    right_child = [0] * (N + 1)

    for arr in in_arr:
        node = int(arr[0])
        if arr[1] not in operator:
            arr[1] = int(arr[1])
        tree[node] = arr[1]
        if len(arr) >= 3:
            left_child[node] = int(arr[2])
            if len(arr) == 4:
                right_child[node] = int(arr[3])

    result = 1
    if operate(1) == 'invalid': result = 0
    print('#{} {}'.format(tc, result))