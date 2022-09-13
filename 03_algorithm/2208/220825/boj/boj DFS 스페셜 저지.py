import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(i):
    global cnt
    while cnt < len(result) and result[cnt] in graph[i]:
        arr.append(result[cnt])
        cnt += 1
        dfs(result[cnt-1])


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
result = list(map(int,input().split()))
cnt = 1
arr = [1]
dfs(1)

if arr == result:
    print(1)
else:
    print(0)