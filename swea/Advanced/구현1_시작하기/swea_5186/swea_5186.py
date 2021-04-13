# 이진수2 D2

# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다.
# 예) 0.625를 이진수로 바꾸면 0.101이 된다.
# N = 0.625
# 0.101
# = 1*2^-1 + 0*2^-2 + 1*2^-3
# = 0.5 + 0 + 0.125
# = 0.625

# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
# 13자리 이상이 필요한 경우에는 'overflow'를 출력하는 프로그램을 작성하시오.

import sys
sys.stdin = open('input_5186.txt')

for tc in range(1, int(input()) + 1):
    N = float(input())

    result = ''
    # 2의 1승부터 ~ 2의 13승까지 계산
    for power in range(-1, -14, -1):
        if 2**power > N:
            result += '0'
        else:
            result += '1'
            N -= (2**power)
        # N == 0 이면 이진수로 변환이 완료된 것 -> 반복문 종료
        if N == 0:
            break
    # 반복문이 강제종료되지 않았다는 것 -> 이진수 변환에 13자리 이상이 필요한 것 -> overflow
    else:
        result = 'overflow'

    print('#{} {}'.format(tc, result))