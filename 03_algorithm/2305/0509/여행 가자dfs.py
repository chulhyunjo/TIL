import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    info = list(map(int,input().rstrip().split()))
    for j in range(N):
        if info[j] == 1:
            graph[i].append(j+1)

plan = list(map(int,input().rstrip().split()))
visited = [False] * (N+1)
answer = 'NO'
def dfs(x, now):
    global visited, answer
    visited[x] =True
    if now == M:
        answer = 'YES'
        return
    if plan[now] in graph[x]:
        visited = [False] * (N+1)
        dfs(plan[now], now+1)
    else:
        for next in graph[x]:
            if not visited[next] and answer == 'NO':
                dfs(next, now)
if N == 1 or M == 1:
    print('YES')
else:
    dfs(plan[0], 1)
    print(answer)