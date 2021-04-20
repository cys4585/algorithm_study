# 병합 정렬

# 병합 정렬을 이용한 오름차순 정렬

# 제약
#   N개의 정렬 대상을 가진 리스트 L을 분할할 때
#   L[0:N//2], L[N//2:N] 으로 분할 한다.
# 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
#   [2, 4, 7, 8], [1, 3, 5, 6]
#   => [1, 2, 3, 4, 5, 6, 7, 8]

# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
# 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.

import sys
sys.stdin = open('input_0504.txt')


def merge_sort(arr):
    global cnt  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt += 1
    # 원소가 1개이면 그냥 그대로 return
    #   이유 : 이미 정렬된 배열임
    if len(arr) == 1:
        return arr
    # 배열의 원소가 2개 이상이면 배열을 두개로 나눠서 각각 정렬된 배열을 return 받는다.
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    l_len = len(left)
    r_len = len(right)
    # idx : 원본 배열의 index
    # l_idx : 왼쪽 배열의 index
    # r_idx : 오른쪽 배열의 index
    idx = l_idx = r_idx = 0
    # 정렬된 왼쪽 배열과 오른쪽 배열을
    # 첫번째 index부터 마지막 index까지 비교하면서 작은 값 부터 가져온다.
    # 두 배열 중 하나라도 탐색이 끝나면 반복문 종료
    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] <= right[r_idx]:
            value = left[l_idx]
            l_idx += 1
        else:
            value = right[r_idx]
            r_idx += 1
        arr[idx] = value
        idx += 1

    # 왼쪽 배열의 탐색이 끝났다면 (즉, 오른쪽 배열에 값이 남아있으면)
    if l_idx == l_len:
        # 가져오지 않은 값들을 다 가져온다.
        for i in range(r_idx, r_len):
            arr[idx] = right[i]
            idx += 1
    # 오른쪽 배열의 탐색이 끝났다면 (즉, 왼쪽 배열에 값이 남아있으면)
    elif r_idx == r_len:
        # 왼쪽 배열의 마지막 원소가 오른쪽 배열의 마지막 원소보다 크기때문에
        # 왼쪽 배열에 값이 남아있는 것이다. -> 카운팅
        cnt += 1
        # 가져오지 않은 값들을 다 가져온다.
        for i in range(l_idx, l_len):
            arr[idx] = left[i]
            idx += 1
    # 병합 정렬된 배열을 리턴
    # 마지막 return인 경우 : 최종적으로 병합 정렬된 배열을 리턴
    # 그렇지 않은 경우 : left or right 변수로 병합 정렬된 중간 결과물을 리턴
    return arr


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = list(map(int, input().split()))

    cnt = 0
    print(f'#{tc} {merge_sort(in_arr)[N//2]} {cnt}')