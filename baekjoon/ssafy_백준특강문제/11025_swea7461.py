# 요세푸스 문제 3

# 1번부터 N번까지 N명이 원을 이룸
# 양의 정수 K가 주어짐 (K <= N)
# K번째 사람을 제거
# N명이 모두 제거될 때 까지 반복
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 함
# ex) (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>

# 마지막으로 남는 사람 구하기

N, K = map(int, input().split())
dead = [0] * N
N -= 1
K -= 1

i = 0
while True:
    idx = i % N
    cnt = 0
    for j in range(idx, len(dead)):
        if dead[j]:
            continue
        cnt += 1
        if cnt == K:
            dead[j] == 1
            break
