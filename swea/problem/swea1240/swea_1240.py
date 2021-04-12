# 단순 2진 암호코드

import sys
sys.stdin = open('input_1240.txt')

pattern = [
    '0001101', '0011001', '0010011', '0111101', '0100011',
    '0110001', '0101111', '0111011', '0110111', '0001011'
]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    in_arr = [list(map(int, input())) for _ in range(N)]

    # 암호 코드 부분 추출
    code = None
    for i in range(N):
        if 1 in in_arr[i]:
            code = in_arr[i]
            break
    # 암호 코드 뒤에 쓰레기 값 제거
    for i in range(M - 1, -1, -1):
        if code[i]:
            break
        code.pop(i)

    arr = []    # 10진수로 변환된 코드를 담을 배열
    # 암호 코드에서 7자리씩 추출
    for i in range(len(code) - 1, -1, -7):
        num = ''
        for j in range(i - 6, i + 1):
            num += str(code[j])
        arr.insert(0, pattern.index(num))   # arr의 0인덱스에 추출한 암호 코드의 십진수를 넣어준다.
        # arr의 길이가 8이 되면 암호 코드 추출 완료 (암호 코드 앞에 쓰레기 값 계산 X)
        if len(arr) == 8:
            break

    result = 0  # 출력값 계산을 위한 변수
    check = 0   # 정상적인 코드인지를 확인하기 위한 변수
    for i in range(len(arr)):
        # 홀수 -> 그냥 더하기
        if i % 2:
            check += arr[i]
        # 짝수 -> 3 곱해서 더하기
        else:
            check += (arr[i] * 3)
        # 출력값 계산
        result += arr[i]

    # 10으로 나누어 떨어지지 않으면 비정상적인 코드
    if check % 10:
        result = 0

    print('#{} {}'.format(tc, result))
