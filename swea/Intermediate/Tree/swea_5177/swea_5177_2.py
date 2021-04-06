# 이진 힙

# 이진 최소힙은 다음과 같은 특징을 가진다.
#   - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
#   - (부모 노드의 값 < 자식 노드의 값)을 유지한다.
#   - 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
#   - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.

import sys
sys.stdin = open('input_5177.txt')

class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self, num):
        if num >= 2:
            if self.lst[num] < self.lst[num // 2]:
                # 자리 바꾸기
                self.lst[num], self.lst[num // 2] = self.lst[num // 2], self.lst[num]
                self.sort(num // 2)  # 계속 정렬

    def append(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def my_sum(self, node):
        if node <= 1:
            return self.lst[node]
        else:
            return self.lst[node] + self.my_sum(node // 2)

    def my_result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2:
            return self.my_sum(last // 2)
        else:
            return 0


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())  # 안씀
    tree = Tree()
    for i in map(int, input().split()):
        tree.append(i)
    print(tree.lst)
    print('#{} {}'.format(test_case, tree.my_result()))