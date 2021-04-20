# 이진 탐색

# 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
# 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

# 전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면,
# 중심 원소의 인덱스 m = (l+r)//2 이고,
# 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

# 이 때 B에 속한 어떤 수가 A에 들어있으면서,
# 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

# 다음은 10개의 정수가 저장된 리스트 A에서 이진 탐색으로 6을 찾는 예이다.
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#      l           m              r     m=4, A[4]=5 < 6 이므로 m의 오른쪽 구간 선택
#                     l     m     r     m=7, A[7]=8 > 6 이므로 m의 왼쪽 구간 선택
#                    l,m r              m=5, A[5]=6 = 6 이므로 탐색 중단

# 6은 탐색 과정에서 양쪽을 번갈아 가며 선택하게 된다.
# 예를 들어 10을 찾는 경우 오른쪽-오른쪽 구간을 선택하므로 조건에 맞지 않는다.
# 5를 찾는 경우 m에 위치하므로 조건에 맞는다.
# 이 때 m에 찾는 원소가 있는 경우 방향을 따지지 않는다.
# M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 프로그램을 만드시오.

import sys
sys.stdin = open('input_5207.txt')


def search(arr, left, right, num, check):
    global check_m
    mid = (left+right) // 2
    if left <= right:
        if arr[mid] == num:
            check_m = 1
            return True
        # 왼쪽
        elif arr[mid] > num:
            if check == 'checked_left':
                return False
            return search(arr, left, mid - 1, num, 'checked_left')
        # 오른쪽
        else:
            if check == 'checked_right':
                return False
            return search(arr, mid + 1, right, num, 'checked_right')
    else:
        return False

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    # print(N, A)
    # print(M, B)
    cnt = 0

    for i in range(M):
        check_l = check_r = 0
        check_m = 0
        if search(A, 0, N - 1, B[i], ''):
            if check_l and check_r:
                cnt += 1
            elif check_m:
                cnt += 1
        # print(B[i], cnt)
    print(f'#{tc} {cnt}')
