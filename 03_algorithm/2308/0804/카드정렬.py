from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    heappush(pq, x)

result = 0
while len(pq) > 1:
    a = heappop(pq)
    b = heappop(pq)
    result += a+b
    heappush(pq, a+b)

print(result)