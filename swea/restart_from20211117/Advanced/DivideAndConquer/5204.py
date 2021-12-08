import sys
sys.stdin = open('./5204_sample_input.txt', 'r')

def merge_sort(arr):
    global cnt
    if len(arr) == 1: return arr

    center = len(arr) // 2
    left = merge_sort(arr[:center])
    right = merge_sort(arr[center:])

    idx = l_idx = r_idx = 0
    l_len, r_len = len(left), len(right)

    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] <= right[r_idx]:
            arr[idx] = left[l_idx]
            l_idx += 1
        else:
            arr[idx] = right[r_idx]
            r_idx += 1
        idx += 1
    if r_idx == r_len:
        cnt += 1
        for i in range(l_idx, l_len):
            arr[idx] = left[i]
            idx += 1
    else:
        for i in range(r_idx, r_len):
            arr[idx] = right[i]
            idx += 1
    return arr


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = list(map(int, input().split()))

    cnt = 0
    result = merge_sort(in_arr)
    print(f'#{tc} {result[N//2]} {cnt}')