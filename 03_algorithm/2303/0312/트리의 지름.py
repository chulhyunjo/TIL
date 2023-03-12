from collections import deque

def bfs(node):
    queue = deque()
    queue.append((node, 0))
    visited[node] = True
    while queue:
        n, d = queue.popleft()
        distance[n] = d
        for nx, dis in tree[n]:
            if not visited[nx]:
                queue.append((nx, d+dis))
                visited[nx] = True

v = int(input())

tree = [[] for _ in range(v+1)]
for _ in range(1,v+1):
    inform = list(map(int, input().split()))
    for i in range(1, len(inform)-1, 2):
        tree[inform[0]].append((inform[i],inform[i+1]))

distance = [0] * (v+1)

visited = [False] * (v+1)
bfs(1)
visited = [False] * (v+1)
max_dis = max(distance)
bfs(distance.index(max_dis))

print(max(distance))