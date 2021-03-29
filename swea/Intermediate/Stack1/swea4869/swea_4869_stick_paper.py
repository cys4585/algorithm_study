import sys
sys.stdin = open("input_4869_stick_paper.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    N = int(input())

    # N = 10 -> 1
    # N = 20 -> 3
    # N = 30 -> 5 (2*1) + 3
    # N = 40 -> 11 (2*3) + 5
    # N = 50 -> (2*5) + 11

    # N = n -> (2*n-2) + n-1 ----->>>> 점화식

    n = N//10
    memory = [1, 1]
    for i in range(2, n+1):
        memory.append(2*memory[i-2] + memory[i-1])
    print('#{} {}'.format(test_case, memory[-1]))