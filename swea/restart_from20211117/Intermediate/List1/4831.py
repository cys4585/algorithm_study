import sys
sys.stdin = open("./4831_sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # K => 한 번 충전으로 최대 이동할 수 있는 정류장 수
    # N => 종점
    # M => 충전소 수
    K, N, M = list(map(int, input().split()))
    charging_stations = list(map(int, input().split()))

    bus_stations = [0] * N
    for i in charging_stations:
        bus_stations[i] = 1
    bus_stations.append(2)  # goal

    bus_now = 0
    energy = K
    cnt = 0
    is_arrival = False
    while not is_arrival:
        max_move = bus_now + K
        for i in range(max_move, bus_now, -1):
            if i >= N:
                is_arrival = True
                break
            elif bus_stations[i] == 1:
                cnt += 1
                bus_now = i
                break
        else:
            result = 0
            break

        if is_arrival:
            result = cnt
            break

    print(f'#{tc} {result}')