# 퀵 정렬

import sys
sys.stdin = open('input_5205.txt')


def partition(arr, left, right):
    pivot = arr[left]
    i = left
    j = right

    while i <= j:
        while i <= j and pivot >= arr[i]:
            i += 1
        while i <= j and pivot <= arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot_idx = partition(arr, left, right)
    quick_sort(arr, left, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, right)


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = list(map(int, input().split()))

    quick_sort(in_arr, 0, len(in_arr) - 1)

    print(f'#{tc} {in_arr[N//2]}')