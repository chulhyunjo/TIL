def dfs(now, arr, first):
    arr.append(now)
    if graph[now] in arr:
        if graph[now] == first:
            for i in arr:
                visited[i] = 1
    else:
        dfs(graph[now],arr,first)

N = int(input())
graph = [0] + list([int(input()) for _ in range(N)])

visited = [0] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, [], i)

print(sum(visited))
for i in range(1, N+1):
    if visited[i] == 1:
        print(i)