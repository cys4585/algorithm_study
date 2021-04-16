# 정식이의 은행업무

# 금액을 2진수와 3진수의 두 가지 형태로 기억하고 있으며,
# 기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한자리만을 잘못 기억하고 있다는 것만은 알고있다.

# 예)
# 현재 기억이 2진수 1010과 3진수 212를 말해주고 있다면
# 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.

# 정식이가 송금액을 추측하는 프로그램을 만들어주자.

# 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.
# 추측할 수 없는 경우는 주어지지 않는다.

import sys
sys.stdin = open('input_4366.txt')


def guess_number(pattern, num_arr, length):
    guess_num = list()
    for i in range(length):
        idx = int(num_arr[i])
        for swap_num in pattern[idx]:
            num_arr[i] = swap_num
            guess_num.append(num_arr[:])
        num_arr[i] = str(idx)
    return guess_num


def swap_to_decimal(jinsu, nums_list, length):
    decimal_nums = list()
    for i in range(len(nums_list)):
        tmp_nums = nums_list[i]
        power = length - 1
        tmp_decimal = 0
        for j in range(len(tmp_nums)):
            tmp_decimal += int(tmp_nums[j]) * (jinsu**power)
            power -= 1
        decimal_nums.append(tmp_decimal)
    return decimal_nums


def find_same_number(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return guess_bin[i]
    return 0


pattern_bin = [['1'], ['0']]
pattern_ter = [['1', '2'], ['0', '2'], ['0', '1']]

for tc in range(1, int(input()) + 1):
    binary_number = list(input())
    ternary_number = list(input())

    N = len(binary_number)
    M = len(ternary_number)

    guess_bin = guess_number(pattern_bin, binary_number, N)
    guess_ter = guess_number(pattern_ter, ternary_number, M)

    guess_bin = swap_to_decimal(2, guess_bin, N)
    guess_ter = swap_to_decimal(3, guess_ter, M)

    result = find_same_number(guess_bin, guess_ter)

    print(f'#{tc} {result}')