# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys
sys.stdin = open("input.txt", "r")


for test_case in range(10):
    T = int(input())
    test_list = list(map(int, input().split()))

    cnt = 0
    for i in range(2, T-2):
        l1 = test_list[i] - test_list[i-2]
        if l1 <= 0:
            continue
        l2 = test_list[i] - test_list[i-1]
        if l2 <= 0:
            continue
        r1 = test_list[i] - test_list[i+1]
        if r1 <= 0:
            continue
        r2 = test_list[i] - test_list[i+2]
        if r2 <= 0:
            continue
        tmp_list = [l1, l2, r1, r2]
        tmp_min = l1
        for j in range(1, len(tmp_list)):
            if tmp_min > tmp_list[j]:
                tmp_min = tmp_list[j]
        cnt += tmp_min

    print('#{} {}'.format(test_case+1, cnt))