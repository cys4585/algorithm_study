# 베이비진 게임

# 0부터 9까지인 숫자 카드 4세트(40장)를 섞은 후 6장의 카드를 골랐을 때,
# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

# 게임을 시작하면 플레이어1과 플레이어2가 교대로 한 장씩 카드를 가져가며,
# 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

# 두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오.
# 만약 무승부인 경우 0을 출력한다.

# 예)
# 9 9 5 6 5 6 1 1 4 2 2 1 인 경우
# 플레이어 1 : 9 5 5 1 4 2
# 플레이어 2 : 9 6 6 1 2 1
# 을 가져가게 된다.
# -> 무승부

import sys
sys.stdin = open('input_5203.txt')


def is_run_or_triplet(cards):
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                # run
                if cards[i] == cards[j] == cards[k]:
                    return True
                # triplet
                sorted_cards = sorted([cards[i], cards[j], cards[k]])
                if sorted_cards[1] == sorted_cards[0] + 1 and sorted_cards[2] == sorted_cards[1] + 1:
                    return True
    return False


for tc in range(1, int(input()) + 1):
    in_cards = list(map(int, input().split()))

    winner = 0

    player_1 = list()
    player_2 = list()
    for idx in range(len(in_cards)):
        if idx % 2 == 0:
            player_1.append(in_cards[idx])
            if len(player_1) >= 3 and is_run_or_triplet(player_1):
                winner = 1
                break
        else:
            player_2.append(in_cards[idx])
            if len(player_2) >= 3 and is_run_or_triplet(player_2):
                winner = 2
                break

    print(f'#{tc} {winner}')