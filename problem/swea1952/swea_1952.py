# 수영장
# 난이도 ?
import sys
sys.stdin = open('input_1952.txt')

def f(M, price):
    global min_price
    if M >= 12: # 모든 달에 대한 계산이 끝났으면
        if price < min_price:   # 최소값 갱신
            min_price = price
        return  # 종료
    if use_plan[M] == 0: return f(M + 1, price) # 이번 달에 이용하는 날이 없으면 종료하면서 다음 달 조사
    for i in range(len(prices)):
        m = M       # 이번 달
        p = price   # 이번 달까지의 비용
        # print(i, m, p)
        if i == 0:  # 1일 이용권
            p += prices[i] * use_plan[m]
            m += 1
        elif i == 1:    # 1달 이용권
            p += prices[i]
            m += 1
        elif i == 2:    # 3달 이용권
            p += prices[i]
            m += 3
        else:   # 1년 이용권
            p = prices[i]
            m = 12
        # print(i, m, p)
        f(m, p)

for tc in range(1, int(input()) + 1):
    # 1일 : 1일 이용 가능
    # 1달 : 매달 1일부터 시작
    # 3달 : 연속된 3달 동안 이용 가능. 매달 1일부터 시작
    # 12달 : 1년 동안 이용 가능. 1월 1일부터 시작
    prices = list(map(int, input().split()))    # 1일 / 1달 / 3달 / 12달 이용권

    use_plan = list(map(int, input().split()))  # 각 달에 며칠 이용할 것인지에 대한 정보
    # print(tc, prices, use_plan)

    # 가장 적인 비용으로 이용할 수 있는 방법 찾기 (가장 적은 비용 출력)
    min_price = 987654321

    f(0, 0)
    print('#{} {}'.format(tc, min_price))