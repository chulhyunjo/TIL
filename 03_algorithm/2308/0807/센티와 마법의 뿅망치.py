import heapq
import sys
input = sys.stdin.readline

N, H, T = map(int,input().split())
pq = []
for _ in range(N):
    height = int(input())
    heapq.heappush(pq, -height) # 최대 힙으로 저장

cnt = 0
# 가장 큰 거인이 H보다 크거나 같거나, 1이 아니거나 뿅마치 개수가 남아 있을 동안 진행
while -pq[0] >= H and -pq[0] != 1 and T != cnt:
    height = -heapq.heappop(pq)
    cnt += 1
    heapq.heappush(pq, -(height//2))

# 가장 큰 거인이 H보다 크거나 같으면 NO
if -pq[0] >= H:
    print('NO')
    print(-pq[0])
else:
    print('YES')
    print(cnt)