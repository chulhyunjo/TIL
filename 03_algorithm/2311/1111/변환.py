from collections import deque

X, Y, A, B = map(int,input().split())

queue = deque([(X, 0)])
visited = [0] * (X+1)
visited[X] = 1
while queue:
    x, cnt = queue.popleft()
    if x == Y:
        print(cnt)
        exit()
    if (x-1)>=0 and not visited[x-1]:
        queue.append((x-1, cnt + 1))
        visited[x-1] = 1
    if x - x%A >=0 and not visited[x-x%A]:
        queue.append(((x - x%A), cnt + 1))
        visited[x - x % A] = 1
    if x - x%B >=0 and not visited[x-x%B]:
        queue.append(((x - x%B), cnt + 1))
        visited[x - x % B] = 1
