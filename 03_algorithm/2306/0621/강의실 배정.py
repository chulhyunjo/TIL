import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    s, e = map(int,input().split())
    heapq.heappush(pq, (s, e))

endTime = []
s, e = heapq.heappop(pq)
heapq.heappush(endTime, e)

while pq:
    s, e = heapq.heappop(pq)
    if s >= endTime[0]:
        heapq.heappop(endTime)
    heapq.heappush(endTime, e)

print(len(endTime))

