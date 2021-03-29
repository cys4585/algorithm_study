import sys
sys.stdin = open("input_1208_flatten.txt", "r")

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    gap = 0
    for _ in range(dump+1):
        min_i = 0
        max_i = 0
        max_v = boxes[0]
        max_v = boxes[0]

        for i, v in enumerate(boxes):
            if max_v < v:
                max_v = v
                max_i = i
            if max_v > v:
                max_v = v
                min_i = i

        gap = boxes[max_i] - boxes[min_i]
        if gap <= 1:
            break

        boxes[max_i] -= 1
        boxes[min_i] += 1

    print('#{} {}'.format(test_case, gap))