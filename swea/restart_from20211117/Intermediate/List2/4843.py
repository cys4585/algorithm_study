import sys
sys.stdin = open('./4843_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a_list = list(map(int, input().split()))

    result_list = []
    for i in range(10):
        if i % 2:   # min
            min_val, min_idx = a_list[0], 0
            for j in range(1, len(a_list)):
                if min_val > a_list[j]:
                    min_val = a_list[j]
                    min_idx = j
            result_list.append(a_list.pop(min_idx))
        else:   # max
            max_val, max_idx = a_list[0], 0
            for j in range(1, len(a_list)):
                if max_val < a_list[j]:
                    max_val = a_list[j]
                    max_idx = j
            result_list.append(a_list.pop(max_idx))

    print(f'#{tc}', *result_list)
