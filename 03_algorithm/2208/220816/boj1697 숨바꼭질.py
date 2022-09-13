from collections import deque
def bfs(n,k):
    queue = deque()
    queue.append([n,0])
    while queue:
        n, cnt = queue.popleft()
        if n == k:
            return cnt
        if n <= 100001:
            if not visited[n]:
                visited[n] = True
                for i in graph[n]:
                    if not visited[i]:
                        queue.append([i,cnt+1])


n, k = map(int,input().split())

graph = [[1]]

for i in range(1,200000):
    graph.append([i-1,i+1,2*i])

visited = [False] * 200000

print(bfs(n,k))