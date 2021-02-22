# 카드 카운팅
# D3
import sys
sys.stdin = open('input_4047.txt')

T = int(input())
for test_case in range(1, T + 1):
    card = input()

    card_dict = {
        'S' : [0] * 14,
        'D' : [0] * 14,
        'H' : [0] * 14,
        'C' : [0] * 14
    }

    for k in range(0, len(card), 3):
        num = int(card[k+1:k+3])
        card_dict[card[k]][num] += 1

    result = None

    card_list = []
    for card in card_dict.values():
        tmp = 0
        for i in range(len(card)):
            if card[i] > 1:
                result = 'ERROR'
                break
            tmp += card[i]
        else:
            card_list.append(13 - tmp)

    if result == 'ERROR':
        print('#{}'.format(test_case), result)
    else:
        print('#{}'.format(test_case), *card_list)
