# 사칙연산

# 사칙연산으로 구성되어 있는 식은 이진 트리로 표현

# 임의의 정점에 연산자가 있으면
# 해당 연산자의 왼쪽 서브 트리(left sub tree)의 결과와
# 오른쪽 서브 트리(right sub tree)의 결과를 사용해서 해당 연산자를 적용한다.

# 사칙연산 '+, -, *, /'와 양의 정수로만 구성된 임의의 이진트리(Binary Tree)가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.

# 단, 중간 과정에서의 연산은 실수 연산으로 하되, 최종 결과ㄱ밧이 정수로 떨어지지 않으면 정수부만 출력한다.

# 정점의 총 수(N)는 1 <= N <= 1000


import sys
sys.stdin = open('input_1232.txt')

# 연산 함수
def operate(v):
    # 양수이면 그냥 리턴
    if not tree[v] in operator:
        return tree[v]

    # 연산자이면 -> left subtree, right subtree 먼저 방문해서 값을 구해온다.
    left = operate(left_child[v])
    right = operate(right_child[v])

    result = None
    if tree[v] == '+': result = left + right
    elif tree[v] == '-': result = left - right
    elif tree[v] == '*': result = left * right
    elif tree[v] == '/': result = left / right
    return result


operator = ['+', '-', '*', '/']

for tc in range(1, 11):
    # 정점(Node)의 총 수
    N = int(input())
    # (노드 번호, 수) or (노드 번호, 연산자, left_child_node, right_child_node)
    in_arr = [input().split() for _ in range(N)]

    tree = [0] * (N + 1)            # 노드에 들어있는 값
    left_child = [0] * (N + 1)      # 노드의 left child 노드 번호
    right_child = [0] * (N + 1)     # 노드의 right child 노드 번호

    for data in in_arr:
        node = int(data[0])     # 노드 번호
        value = data[1]         # 노드의 값
        # 연산자이면
        if value in operator:
            tree[node] = value                  # 값
            left_child[node] = int(data[2])     # left child 노드 번호
            right_child[node] = int(data[3])    # right child 노드 번호
        # 양수이면
        else:
            tree[node] = int(value)             # 값

    # 최종 연산 후, int 타입으로 변환
    print('#{} {}'.format(tc, int(operate(1))))