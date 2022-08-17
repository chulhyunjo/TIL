def dfs(v, N):
    visited = [0] * N
    stack = [0] * N
    top = -1
    print(v)                    # 방문
    visited[v] = 1              # 시작점 방문 표시
    while True:
        for w in adjList[v]:    # if(v의 인접정범 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1            #push
                stack[top] = v      #push
                v = w
                print(v)
                visited[w] = 1
                break
        else:                   # w가 없으면
            if top != -1:
                v = stack[top]  # pop
                top -= 1
            else:               # 스택이 비어있으면
                break


V, E = map(int,input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
stack = [0] * N
dfs(1,N)
print()