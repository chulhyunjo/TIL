import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]


def nodeHeight():
    queue = deque()
    queue.append((1,0))
    while queue:
        now, height = queue.popleft()
        for nxt in tree[now]:
            if not visited[nxt]:
                queue.append((nxt, height+1))
                node_height[nxt] = height+1
                tree_parents[nxt] = now
                visited[nxt] = True


for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (N+1)
visited[1] = True

node_height = [0] * (N+1)
tree_parents = [0] * (N+1)
nodeHeight()

M = int(input())
for _ in range(M):
    a, b = map(int,input().split())
    if node_height[a] < node_height[b]:
        a, b = b, a

    while node_height[a] != node_height[b]:
        a = tree_parents[a]

    while a != b:
        a = tree_parents[a]
        b = tree_parents[b]

    print(a)

