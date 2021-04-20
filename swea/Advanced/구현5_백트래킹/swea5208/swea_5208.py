# 전기버스2

# 충전지를 교환하는 방식의 전기버스를 운행하려고 한다.

# 정류장에는 교체용 충전기가 있는 교환기가 있고,
# 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.

# 충전지가 방전되기 전에 교체하며 운행해야 하는데,
# 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.

# 정류장과 충전지에 대한 정보가 주어질 때,
# 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오.
# 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

# 다음은 1번에서 출발 5번이 종점이 경우의 예이다.
# 정류장 : 1 2 3 4 5
# 충전지 : 2 3 1 1
# 1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다.
# 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.

import sys
sys.stdin = open('input_5208.txt')


# bus : 버스의 위치 (정류장)
# energy : 이동 가능 횟수
# replace : 충전지를 교체할지 말지 True or False
# cnt : 충전지를 교체한 횟수
def move(bus, energy, replace, cnt):
    global min_cnt
    # 목적지에 도착했다면
    if bus == N - 1:
        # 최소 교체 횟수를 갱신
        if min_cnt > cnt:
            min_cnt = cnt
        return
    # 목적지에 도착하기도 전에 최소 교체 횟수를 넘어섰다면 -> back (퇴각)
    elif cnt > min_cnt:
        return
    # replace == True 이면 충전지를 교체하는 것
    if replace:
        # cnt 증가시키고, energy 갱신
        cnt += 1
        energy = battery[bus]
    # energy가 0이면 더이상 이동할 수 없다는 뜻 -> back (퇴각)
    if energy == 0:
        return
    # 다음 정류장으로 이동하면서, energy 1 소모시키고,
    # 다음 정류장에서 충전지 교체를 하는 경우와 안하는 경우를 각각 탐색
    move(bus + 1, energy - 1, False, cnt)
    move(bus + 1, energy - 1, True, cnt)


for tc in range(1, int(input()) + 1):
    battery = list(map(int, input().split()))
    N = battery.pop(0)

    min_cnt = 987654321
    move(0, 0, True, 0)

    print('#{} {}'.format(tc, min_cnt - 1))