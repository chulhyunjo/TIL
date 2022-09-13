T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int,input().split()) # k:갈 수 있는 거리 , n: 노선 길이, m: 정류장 수
    charge = list(map(int, input().split()))

    bus_line = [0] * (n+1) # 전체 노선을 받을 리스트 (0~n)정류장
    for i in range(m):
        bus_line[charge[i]] = 1

    result = 0 # 충전 횟수 받을 변수
    cnt = 0
    charge = 0

    # 1~n k만큼 이동할 때마다 충전 1회 필요
    for i in range(1, n+1, k):
        cnt = i
        if cnt + k >= n:
            break
        # 버스가 움직일 수 있는 거리가 k이므로 0(출발점)을 제외하고 k씩 받아 온다
        distance = bus_line[i: i+k]
        # 최대 거리를 기준으로 반대로 충전기가 있는 경우 충전-> break
        for j in range(k-1, -1, -1):
            if distance[j] == 1:
                result += 1
                charge = cnt + j
                break
        # 충전을 못했을 경우 break가 선언x
        # 충전을 못하면 갈 수 없는 노선-> 0출력 break
        else:
            result = 0
            break

    while cnt <= n:
        if cnt - charge >k :
            result = 0
            break
        if bus_line[cnt] == 1:
            result += 1
            break
        cnt += 1

    print(f'#{tc} {result}')
