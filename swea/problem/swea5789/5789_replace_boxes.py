import sys

sys.stdin = open("input_5789_replace_boxes.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N : 상자의 개수 (1~N)
    # Q : 반복 횟수
    N, Q = map(int, input().split())

    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            boxes[j] = i

    print('#{}'.format(test_case), end=' ')
    for box in boxes:
        print(box, end=' ')
    print()
