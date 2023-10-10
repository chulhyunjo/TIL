import heapq
import sys
input = sys.stdin.readline

N = int(input())

pq = []
cnt = 0
for i in range(N):
    lst = list(map(int,input().split()))
    for j in lst:
        heapq.heappush(pq, j)
        cnt += 1

    while cnt > N:
        heapq.heappop(pq)
        cnt -= 1

print(pq[0])