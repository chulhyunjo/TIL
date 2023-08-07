import heapq

N, M = map(int,input().split())
times = list(map(lambda x: -int(x) ,input().split()))
heapq.heapify(times) # 최소 힙

time = 0            # 현재 시간
cnt = 0             # 충전기 사용 개수
pq = []             # 충전기 사용 리스트
finish = 0

while True:
    # 충전기 사용 중이고 완료됐으면 삭제
    while cnt and time >= pq[0]:
        heapq.heappop(pq)
        cnt -= 1
        finish += 1
    # 충전기 자리가 비어있고 전자기기가 남아 있다면
    while times and cnt < M:
        cnt += 1
        # 완료되는 시간을 최소 힙에 저장
        heapq.heappush(pq, (time - heapq.heappop(times)))

    # 충전기 완료 되었으면 종료
    if finish == N:
        break

    # 충전기가 다 사용 중이라면 현재 시간 -> 다음 충전 완료되는 시간으로 이동
    if cnt == M:
        time = pq[0]
    # 아니면 +1
    else:
        time += 1

print(time)