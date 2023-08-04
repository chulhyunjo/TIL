from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append((x, 0))
    visited[x] = True
    while queue:
        n, d = queue.popleft()
        distance[n] = d
        for dis, nx in tree[n]:
            if not visited[nx]:
                queue.append((nx, d+dis))
                visited[nx] = True

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    num, *node = map(int,input().split())
    node.pop()
    for i in range(0,len(node),2):
        tree[num].append((node[i+1], node[i]))

visited = [False] * (V+1)
distance = [0] * (V+1)
bfs(1)
visited = [False] * (V+1)
max_dis = max(distance)
bfs(distance.index(max_dis))
print(max(distance))