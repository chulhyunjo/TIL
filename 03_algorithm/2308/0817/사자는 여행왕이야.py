import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

pq = []
start = 1
for _ in range(M):
    s, e = map(int,input().split())
    heapq.heappush(pq, (e, s))

answer = 0
while pq:
    e, s = heapq.heappop(pq)
    if start < s:
        answer = max(answer, s - start -1)
        start = e

print(answer)