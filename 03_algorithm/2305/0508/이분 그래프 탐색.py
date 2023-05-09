import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

K = int(input().rstrip())

def dfs(s):
    global answer
    visited[s] = True
    for next in graph[s]:
        if not visited[next]:
            checkNode[next] = (checkNode[s]+1)%2
            dfs(next)
        elif checkNode[s] == checkNode[next]:
            answer = 'NO'



for _ in range(K):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    checkNode = [0] * (V+1)
    visited = [False] * (V+1)
    answer = 'YES'

    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1):
        if answer == 'YES':
            dfs(i)
        else:
            break

    print(answer)