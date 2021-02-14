import sys

sys.stdin = open("input_4831_electronic_bus.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # # K : 한번 충전으로 이동할 수 있는 정류장 수
    # # N : 종점 정류장
    # # M : 충전기가 설치된 정류장 갯수
    # K, N, M = map(int, input().split())
    # # charging_list : 충전기가 설치된 정류장 번호
    # charging_list = list(map(int, input().split()))
    #
    # # 내가 푼 풀이
    # # energy : 버스의 남은 에너지 (이동할 수 있는 거리만큼)
    # # cnt : 충전횟수
    # energy = K
    # cnt = 0
    #
    # # bus : 버스의 위치
    # for bus in range(1, N+1):
    #     energy -= 1
    #
    #     if bus in charging_list:
    #         i = charging_list.index(bus)
    #         if i != M - 1:
    #             if energy < charging_list[i+1] - charging_list[i]:
    #                 cnt += 1
    #                 energy = K
    #         else:
    #             if bus + energy < N:
    #                 cnt += 1
    #                 energy = K
    #     elif bus < N and energy <= 0:
    #         cnt = 0
    #         break
    #
    # print('#{} {}'.format(test_case, cnt))

    # # 수업에서 푼 풀이
    # K, N, M = map(int, input().split())
    # charge = list(map(int, input().split()))
    #
    # bus_stop = [0] * (N+1)  # 버스 정류장
    #
    # # 버스 정류장 중 충전소가 있는 곳을 표시
    # for i in charge:
    #     bus_stop[i] = 1
    #
    # bus = 0 # 버스 위치
    # ans = 0 # 충전 횟수
    #
    # while True:
    #     # 버스가 이동할 수 있는만큼 이동
    #     bus += K
    #     if bus >= N: break # 종점에 도착하거나 종점지를 지난 경우 종료
    #
    #     for i in range(bus, bus-K, -1):
    #         if bus_stop[i]:
    #             ans += 1
    #             bus = i
    #             break
    #     # 충전기를 못찾았을 때 (for-else 문...?)
    #     else:
    #         ans = 0
    #         break
    #
    # print('#{} {}'.format(test_case, ans))

    # 수업에서 푼 풀이 2
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    ans = 0

    charge = [0] + charge + [N]
    # charge.insert(0, 0)
    # charge.append(N)

    last = 0

    # 충전소에 출발점과 도착지를 넣어놓았으므로
    for i in range(1, M+2):
        if charge[i] - charge[i-1] > K:
            ans = 0
            break

        # 갈 수 있으면 아무 작업 x
        # 갈수 없으면 바로 직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1

    print('#{} {}'.format(test_case, ans))