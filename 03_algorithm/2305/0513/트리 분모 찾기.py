import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    visited[x] = True
    for i in tree[x]:
        if not visited[i]:
            answer[i] = x
            dfs(i)

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
for i in range(2, N+1):
    print(answer[i])