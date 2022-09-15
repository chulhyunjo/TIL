from collections import deque

x, y = map(int,input().rstrip().split())
queue = deque()
queue.append(x)
visited = [-1] * 100001
visited[x] = 0
while queue:
    x = queue.popleft()
    if x == y:
        print(visited[x])
        break
    if 0 <= 2*x < 100001 and visited[2*x] == -1:
        queue.appendleft(2*x)
        visited[2*x] = visited[x]
    if 0 <= x+1 < 100001 and visited[x+1] == -1:
        queue.append(x+1)
        visited[x+1] = visited[x]+1
    if 0 <= x-1 and visited[x-1] == -1:
        queue.append(x-1)
        visited[x-1] = visited[x] +1