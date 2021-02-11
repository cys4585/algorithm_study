import sys

sys.stdin = open("input_4836_coloring.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N : 칠할 영역의 개수
    N = int(input())
    draws_red = []
    draws_blue = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp[2] += 1
        tmp[3] += 1
        if tmp[4] == 1:
            draws_red.append(tmp[:4])
        else:
            draws_blue.append(tmp[:4])

    purple_box = 0
    for blue in draws_blue:
        blue_r1, blue_c1, blue_r2, blue_c2 = blue
        for red in draws_red:
            purple_width = 0
            purple_height = 0
            red_r1, red_c1, red_r2, red_c2 = red

            if red_r1 < blue_r1 < red_r2 and red_r1 < blue_r2 < red_r2:
                purple_height = blue_r2 - blue_r1
            elif blue_r1 < red_r1 < blue_r2 and blue_r1 < red_r2 < blue_r2:
                purple_height = red_r2 - red_r1
            elif red_r1 < blue_r1 < red_r2:
                purple_height = red_r2 - blue_r1
            elif red_r1 < blue_r2 < red_r2:
                purple_height = blue_r2 - red_r1

            if red_c1 < blue_c1 < red_c2 and red_c1 < blue_c2 < red_c2:
                purple_width = blue_c2 - blue_c1
            elif blue_c1 < red_c1 < blue_c2 and blue_c1 < red_c2 < blue_c2:
                purple_width = red_c2 - red_c1
            elif red_c1 < blue_c1 < red_c2:
                purple_width = red_c2 - blue_c1
            elif red_c1 < blue_c2 < red_c2:
                purple_width = blue_c2 - red_c1

            purple_box += purple_width * purple_height

    print('#{} {}'.format(test_case, purple_box))