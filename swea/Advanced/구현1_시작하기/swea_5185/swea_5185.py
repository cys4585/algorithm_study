# 이진수 D2

# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오
# 단, 2진수의 앞자리 0도 반드시 출력한다
# 예) 47FE -> 0100011111111110

import sys
sys.stdin = open('input_5185.txt')


# 16진수 -> 10진수
def hex_to_decimal(n):
    if ord('0') <= ord(n) <= ord('9'):
        return ord(n) - ord('0')
    return ord(n) - ord('A') + 10

# 10진수 -> 2진수
def decimal_to_binary(n):
    binary = ''
    for power in range(3, -1, -1):
        binary += str(n // (2**power))
        n %= (2**power)
    return binary


for tc in range(1, int(input()) + 1):
    N, in_num = input().split()
    N = int(N)

    result = ''
    for num in in_num:
        # 16진수 -> 10진수 -> 2진수 -> 합치기
        result += decimal_to_binary(hex_to_decimal(num))

    print('#{} {}'.format(tc, result))

