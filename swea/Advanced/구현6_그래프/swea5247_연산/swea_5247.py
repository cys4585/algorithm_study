# 연산 (D4)

# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이
# +1, -1, *2, -10
# 네 가지라고 할 때, 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
# 단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

import sys
sys.stdin = open('input_5247.txt')

from collections import deque

def add_1(n):
    return n + 1
def sub_1(n):
    return n - 1
def mul_2(n):
    return n * 2
def sub_10(n):
    return n - 10
calculate = [mul_2, sub_10, add_1, sub_1]

def my_func_bfs(n):
    queue = deque()
    queue.append((n, 0))
    nums_set = set()
    while queue:
        num, cnt = queue.popleft()
        if num in nums_set:
            continue
        nums_set.add(num)
        if num == M:
            return cnt
        for i in range(4):
            tmp = calculate[i](num)
            if 1 <= tmp <= 1000000:
                queue.append((tmp, cnt + 1))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # N != M
    # 1 <= N, M <= 1,000,000
    print(f'#{tc} {my_func_bfs(N)}')
