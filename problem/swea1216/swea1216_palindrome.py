import sys
sys.stdin = open("input_1216_palindrome.txt", "r")

T = 10
for test_case in range(1, T + 1):
    tc = input()
    arr = [input() for _ in range(100)]
    N = len(arr)

    pal_len = len(arr)

    result = 0
    breaker = False

    while pal_len > 0:
        for i in range(N):
            for j in range(N - pal_len + 1):
                tmp_str_x = ''
                tmp_str_y = ''
                for k in range(j, j + pal_len):
                    tmp_str_x += arr[i][k]
                    tmp_str_y += arr[k][i]

                for k in range(len(tmp_str_x)//2):
                    if tmp_str_x[k] != tmp_str_x[-1-k]:
                        break
                else:
                    result = len(tmp_str_x)
                    breaker = True
                    break

                for k in range(len(tmp_str_y)//2):
                    if tmp_str_y[k] != tmp_str_y[-1-k]:
                        break
                else:
                    result = len(tmp_str_y)
                    breaker = True
                    break
            if breaker:
                pal_len = 0
                break
        pal_len -= 1

    print('#{} {}'.format(test_case, result))