# 소풍

# 무대 1~N번 (N명) 시계방향 원형
# KIN 게임
    # 1번부터 시작, 시계방향으로 K까지 셈
    # K를 말하면 퇴장
    # 다음 자리부터 다시 1부터 시작
    # 동호 : M번
    # 동호가 퇴장당하는 순서 구하기

N, K, M = input().split()
M -= 1
alive = [1] * N
out_cnt = 0
