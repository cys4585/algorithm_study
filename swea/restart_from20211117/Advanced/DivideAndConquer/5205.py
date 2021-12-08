import sys
sys.stdin = open('./5205_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = list(map(int , input().split()))

    quick_sort(in_arr, 0, len(in_arr) -1 )