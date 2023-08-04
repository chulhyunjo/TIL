import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    s, e = map(int,input().split())
    heapq.heappush(pq, (e, s))

endTime = 0
answer = 0
while pq:
    e, s = heapq.heappop(pq)
    if endTime <= s:
        endTime = e
        answer += 1

print(answer)