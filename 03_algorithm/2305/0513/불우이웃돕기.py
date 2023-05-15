import heapq

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x
        return True
    else:
        return False

N = int(input())
pq = []
sum1 = 0
parents = list(range(N+1))

for i in range(N):
    line = input()
    for j in range(N):
        if line[j] == '0': continue
        else:
            length = ord(line[j])
            if 65 <= length <= 90:
                length = length % 65 + 27
                heapq.heappush(pq,(length, i, j))
            else:
                length = length % 97 + 1
                heapq.heappush(pq,(length, i, j))
            sum1 += length

nodes = 0
while pq and nodes < N-1:
    length, x, y = heapq.heappop(pq)
    if x == y: continue
    if union(x,y):
        sum1 -= length
        nodes += 1
if nodes == N-1:
    print(sum1)
else:
    print(-1)