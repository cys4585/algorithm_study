# 암호코드 스캔

# 암호 코드 규칙
# 1. 총 8개의 숫자로 이루어져 있다.
# 앞 7자리는 상품 고유 번호, 마지막 자리는 검증 코드
#   - 검증코드는 아래와 같은 방법으로 계산
#   "(홀수 자리의 합 * 3) + 짝수 자리의 합 + 검증 코드"가 10의 배수
#   상품 고유 번호가 8801234일 경우,
#   (8 + 0 + 2 + 4) * 3 + 8 + 1 + 3 + 검증코드
#   = 42 + 12 + 검증코드
#   = 54 + 검증코드 = 10의 배수
#   검증코드 = 6 일 때만 정상적인 암호코드
#   검증코드가 6이 아니면 비성장적인 암호코드

# 세로 2000, 가로 500 이하의 크기를 가진 직사각형 배열에 암호코드 정보가 포함되어 전달된다.
# 이 때, 하나의 배열에는 1개 이상의 암호코드가 존재한다.
# (단, 모든 암호코드가 정상적인 암호코드임을 보장할 수 없다. 비정상적인 암호코드가 포함될 수 있다.)

# 배열은 16진수로 이루어져 있다. 이 배열을 2진수로 변환하여 그 안에 포함되어 있는 암호코드 정보를 확인한다.

# 포함된 암호코드들의 검증코드를 확인하여 정상적인 암호코드인지 확인한다.
# 정상적인 암호코드들을 판별한 뒤 이 함호코드들에 적혀있는 숫자들의 합을 출력한다.
# 이 때, 총 소요시간이 적을수록 성능이 좋은 것으로 간주된다.

# 배열에 포함되어 있는 암호코드의 세부 규칙은 다음과 같다.
# 1. 암호코드 하나는 숫자 8개로 구성되며 시작 구분선, 종료 구분선은 별도로 존재하지 않는다.
# 2. 암호코드들이 붙어있는 경우는 존재하지 않는다. (각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다.)
# 3. 암호코드가 일부만 표시된 경우는 없다. 모든 암호코드는 8개의 숫자로 구성되어 있다.
# 4. 암호코드의 세로 길이는 5 ~ 100 칸이다.
# 5. 암호코드의 가로 길이는 암호코드 선의 두께에 따라 달라지며, 두께가 가장 가는 경우,
#    숫자 하나가 차지하는 길이는 7칸이다. 각 숫자들을 글미으로 표시하는 방법은 다음과 같다.
# 0 : 3,2,1,1 (0001101)
# 1 : 2,2,2,1 (0011001)
# 2 : 2,1,2,2 (0010011)
# 3 : 1,4,1,1 (0111101)
# 4 : 1,1,3,2 (0100011)
# 5 : 1,2,3,1 (0110001)
# 6 : 1,1,1,4 (0101111)
# 7 : 1,3,1,2 (0111011)
# 8 : 1,2,1,3 (0110111)
# 9 : 3,1,1,2 (0001011)

# 암호코드의 가로 길이가 길어질 경우, 숫자 하나가 차지하는 길이는 7의 배수가 된다.
# 예를 들어, 가로 길이가 2배가 될 경우 9는 아래와 같이 표시될 수 있다.
# 3,1,1,2 (00000011001111)

# 6. 암호코드 하나의 최소 길이는 56이며, 암호코드 선이 굵어질 경우, 56의 배수의 길이를 갖게 된다.
#    예를들어 암호코드 숫자 하나가 14칸을 사용하는 경우, 암호코드 하나의 가로길이는 112가 된다. 암호코드 하나에
#    포함되는 암호코드 숫자들은 모두 동일한 크기를 갖는다.

import sys
sys.stdin = open('input_1242.txt')

# # 16진수 -> 10진수 (1자리 수 계산)
# def hex_to_decimal(hex_n):
#     hex_n = ord(hex_n)
#     zero = ord('0')
#     nine = ord('9')
#     if zero <= hex_n <= nine:
#         return hex_n - zero
#     a = ord('A')
#     return hex_n - a + 10
#
#
# # 10진수 -> 2진수 (1자리 수 계산)
# def decimal_to_binary(decimal_n):
#     binary = ''
#     for power in range(3, -1, -1):
#         binary += str(decimal_n // (2**power))
#         decimal_n = (decimal_n % (2**power))
#     return binary
#
#
# # 16진수 암호코드 -> 2진수 암호코드 (한 줄 전체를 변환)
# def code_to_binary(in_str):
#     binary = ''
#     for char in in_str:
#         binary += decimal_to_binary(hex_to_decimal(char))
#     return binary


pattern = [
    (3, 2, 1, 1), (2, 2, 2, 1), (2, 1, 2, 2), (1, 4, 1, 1), (1, 1, 3, 2),
    (1, 2, 3, 1), (1, 1, 1, 4), (1, 3, 1, 2), (1, 2, 1, 3), (3, 1, 1, 2)
]

# 코드 부분만 추출하기
def extract_decimal_code(in_str):
    code = list()   # 10진 암호 코드 하나하나씩 저장할 배열 (8개 채우면 빈 배열로 리셋)
    idx = len(in_str) - 1
    # in_str의 뒤->앞으로 역순으로 조사
    while idx >= 0:
        # 1을 만나면 그 때부터 암호코드 추출 시작
        if in_str[idx] == '1':
            # 0001101 이면
            # n1=3 / n2=2 / n3=1 / n4=1
            n1 = n2 = n3 = n4 = 0
            # n4 추출
            while in_str[idx] == '1':
                n4 += 1
                idx -= 1
            # n3 추출
            while in_str[idx] == '0':
                n3 += 1
                idx -= 1
            # n2 추출
            while in_str[idx] == '1':
                n2 += 1
                idx -= 1
            # n1 추출 (n1이 어디까지인지 알 수 없기 때문에
            # 전체 크기인 (7*multiple)에서 n2 n3 n4를 빼면 -> n1
            #   multiple은 배수 (전체 크기가 7, 14, 21, 28 ... 이기 때문)
            multiple = min(n2, n3, n4)
            n1 = (7 * multiple) - (n2 + n3 + n4)
            # 암호 코드 끝나는 부분으로 idx 옮기기
            idx -= n1
            # 배율 빼주기
            #   6 : 4 : 2 : 2 인 경우 -> 3 : 2 : 1 : 1 로 바꿔줌
            n1 //= multiple
            n2 //= multiple
            n3 //= multiple
            n4 //= multiple
            # 3 : 2 : 1 : 1 -> 십진수로 얻기 (원소의 인덱스가 십진수)
            decimal_num = pattern.index((n1, n2, n3, n4))
            # 새로 얻은 십진수를 앞으로 넣는다 (뒤에서 부터 조사했기 때문)
            code.insert(0, decimal_num)
            # 암호 코드 한 세트를 추출했으면 -> 암호 코드 추가해주고, 코드를 담을 변수는 리셋
            if len(code) == 8:
                if ((code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]) % 10 == 0:
                    if code not in decimal_codes:
                        decimal_codes.append(code)
                code = list()
        # 암호와 상관없는 부분은 그냥 패스
        else:
            idx -= 1


hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    in_arr = [input() for _ in range(N)]
    in_arr = list(set(in_arr))  # 중복 row 제거

    decimal_codes = list()
    for i in range(len(in_arr)):
        arr = in_arr[i]
        for j in range(M):
            if arr[j] != '0' or arr[len(arr) - i - 1] != '0':
                # 16진 코드 -> 2진 코드 변환
                binary_code = ''
                for k in range(M):
                    binary_code += hex_to_bin[arr[k]]
                binary_code = binary_code.rstrip('0')
                # 2진 코드 -> 10진수 코드 변환 (유효성 검사, 중복 검사 포함)
                extract_decimal_code(binary_code)
                break
    result = 0
    code_length = len(decimal_codes)
    for i in range(code_length):
        result += sum(decimal_codes[i])

    print('#{} {}'.format(tc, result))