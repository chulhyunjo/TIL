import heapq

n = int(input())
rope = []

for _ in range(n):
    l = int(input())
    heapq.heappush(rope, -l)

answer = 0

for i in range(1,n+1):
    n = -heapq.heappop(rope)
    fullWeight = n * i
    if answer < fullWeight:
        answer = fullWeight

print(answer)