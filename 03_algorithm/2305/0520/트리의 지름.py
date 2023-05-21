from collections import deque
import sys
input = sys.stdin.readline

def findDistance(idx, distance):
    queue = deque()
    queue.append((idx,0))
    visited[idx] = True

    while queue:
        now, d = queue.popleft()
        distance[now] = d
        for next, dis in tree[now]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, d+dis))

n = int(input())
tree = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    par, chi, l = map(int,input().split())
    tree[par].append((chi,l))
    tree[chi].append((par,l))

findDistance(1, distance)

max_idx = distance.index(max(distance))
answer = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
findDistance(max_idx, answer)
print(max(answer))