import sys
sys.stdin = open('./5203_sample_input.txt', 'r')

def check_run(cards):
    if cards[0] == cards[1] == cards[2]: return True
    return False

def check_triplet(cards):
    tmp = sorted(cards)
    if tmp[0] + 2 == tmp[1] + 1 == tmp[2]: return True
    return False

def check_baby_gin(cards):
    if len(cards) < 3: return False
    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) - 1):
            for k in range(j + 1, len(cards)):
                c = [cards[i], cards[j], cards[k]]
                if check_run(c) or check_triplet(c): return True
    return False


for tc in range(1, int(input()) + 1):
    all_cards = list(map(int, input().split()))

    player1, player2 = [], []
    turn = True
    result = 0
    for card in all_cards:
        if turn: player1.append(card)
        else: player2.append(card)
        p1_baby_gin = check_baby_gin(player1)
        p2_baby_gin = check_baby_gin(player2)
        if p1_baby_gin and not p2_baby_gin:
            result = 1
            break
        elif not p1_baby_gin and p2_baby_gin:
            result = 2
            break
        turn = not turn

    print(f'#{tc} {result}')