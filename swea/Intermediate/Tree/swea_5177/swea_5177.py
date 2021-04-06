# 이진 힙

# 이진 최소힙은 다음과 같은 특징을 가진다.
#   - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
#   - (부모 노드의 값 < 자식 노드의 값)을 유지한다.
#   - 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
#   - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.

import sys
sys.stdin = open('input_5177.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    in_arr = list(map(int, input().split()))
    in_arr.insert(0, 0)

    flag = True
    while flag:
        flag = False
        for i in range(1, N + 1):
            left, right = 2 * i, 2 * i + 1
            if left <= N and right <= N:
                print(i, in_arr[i], in_arr[left], in_arr[right])
            if left > N: continue
            if in_arr[left] < in_arr[i]:
                in_arr[i], in_arr[left] = in_arr[left], in_arr[i]
                flag = True
            if right > N: continue
            if in_arr[right] < in_arr[i]:
                in_arr[i], in_arr[right] = in_arr[right], in_arr[i]
                flag = True
            print(i, in_arr[i], in_arr[left], in_arr[right])
        print(in_arr)

    node = N
    sum_v = 0
    while node >= 1:
        node //= 2
        sum_v += in_arr[node]
    print(in_arr)
    print('#{} {}'.format(tc, sum_v))

