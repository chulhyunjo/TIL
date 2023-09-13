import heapq

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
pq = []
for n in numbers:
    heapq.heappush(pq, n)

answer = 0
for _ in range(M):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    heapq.heappush(pq, a+b)
    heapq.heappush(pq, a+b)

print(sum(pq))