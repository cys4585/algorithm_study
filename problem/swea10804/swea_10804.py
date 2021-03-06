# 문자열의 거울상
# D3
import sys
sys.stdin = open("input_10804.txt")
for tc in range(1, int(input()) + 1):
    in_arr = list(map(str, input()))
    # print(in_arr)

    for i in range(len(in_arr)):
        if in_arr[i] == 'b': in_arr[i] = 'd'
        elif in_arr[i] == 'd': in_arr[i] = 'b'
        elif in_arr[i] == 'p': in_arr[i] = 'q'
        else: in_arr[i] = 'p'

    print("#{}".format(tc), end=" ")
    for _ in range(len(in_arr)):
        print(in_arr.pop(), end="")
    print()