from collections import deque

x, y, z = list(map(int,input().split()))
visited = [[False] * (y+1) for _ in range(x+1)]
queue = deque()
queue.append((0,0,z))
visited[0][0] = True
result = []
while queue:
    a, b, c= queue.popleft()
    if a == 0:
        result.append(c)

    if a > 0 and y - b > 0: # a->b
        next_w = min(a, y-b)
        if not visited[a-next_w][b + next_w]:
            visited[a-next_w][b + next_w] = True
            queue.append((a-next_w, b + next_w, c))
    if b > 0 and x - a > 0: # b->a
        next_w = min(b, x - a)
        if not visited[a+next_w][b-next_w]:
            visited[a+next_w][b-next_w] = True
            queue.append((a+next_w, b-next_w, c))
    if a > 0 and z - c > 0: # a->c
        next_w = min(a, z-c)
        if not visited[a-next_w][b]:
            visited[a-next_w][b] = True
            queue.append((a-next_w, b, c+next_w))
    if b > 0 and z - c > 0: # b->c
        next_w = min(b, z-c)
        if not visited[a][b-next_w]:
            visited[a][b-next_w] = True
            queue.append((a, b-next_w, c+next_w))
    if c > 0 and x - a > 0: # c->a
        next_w = min(c, x-a)
        if not visited[a+next_w][b]:
            visited[a+next_w][b] = True
            queue.append((a+next_w, b, c-next_w))
    if c > 0 and y - b > 0: # c->b
        next_w = min(c, y-b)
        if not visited[a][b+next_w]:
            visited[a][b+next_w] = True
            queue.append((a, b+next_w, c-next_w))

print(*sorted(result))