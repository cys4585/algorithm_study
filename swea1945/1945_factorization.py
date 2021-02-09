import sys

sys.stdin = open("input_1945_factorization.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while True:
        if N % 2 == 0:
            N /= 2
            a += 1
        elif N % 3 == 0:
            N /= 3
            b += 1
        elif N % 5 == 0:
            N /= 5
            c += 1
        elif N % 7 == 0:
            N /= 7
            d += 1
        elif N % 11 == 0:
            N /= 11
            e += 1
        else:
            break
    print('#{} {} {} {} {} {}'.format(test_case, a, b, c, d, e))