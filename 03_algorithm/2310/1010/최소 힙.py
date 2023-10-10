import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    n = int(input())
    if n == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, n)
