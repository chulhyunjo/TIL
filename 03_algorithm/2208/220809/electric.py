T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    bus_line = [0] * (n+1) # 전체 노선
    for i in charge:
        bus_line[i] = 1

    location = 0 # 현재 위치
    result = 0 # 충전 횟수
    while True:
        area = bus_line[location: location+k+1]
        for i in range(k, 0, -1): # 충전기 확인
            if area[i] == 1:
                result += 1
                location += i # 이동
                break
        else: # 없을 경우
            result = 0
            break
        if location + k >= n:
            break

    print(f'#{tc} {result}')