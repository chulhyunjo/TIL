from collections import deque

x, y, z = list(map(int,input().split()))
visited = [[False] * (y+1) for _ in range(x+1)]
queue = deque()
queue.append((0,0,z))
visited[0][0] = True    # C물통만 가득차 있으므로 A,B물의 양으로 C물통의 양을 알 수 있다.
                        # A, B 물통에 들어간 물의 양은 한정적이다.
result = [] # A가 비었을 때 C물통에 담겨 있을 수 있는 물의 양을 담을 리스트
while queue:
    a, b, c= queue.popleft()    # 현재 A, B, C 물통의 물 양 = a, b, c
    if a == 0:                  # A가 비어있을 때 C에 담겨 있는 물의 양을 출력해야 하므로
        result.append(c)        # 결과 리스트에 C 물통의 양을 담기

    if a > 0 and y - b > 0: # A에 물이 있고 B에 물이 들어갈 수 있는 경우 A->B로 물 옮기기
        next_w = min(a, y-b)    # A->B에 (A 안의 물의 양, B에 들어갈 수 있는 물의 양) 중 작은 값 만큼 쏟아서 부을 수 있다.
        if not visited[a-next_w][b + next_w]:   # 쏟아 부었을때 A, B 물통의 물의 양을 탐색 하지 않은 경우만 담기
            visited[a-next_w][b + next_w] = True
            queue.append((a-next_w, b + next_w, c))
    if b > 0 and x - a > 0: # B->A
        next_w = min(b, x - a)
        if not visited[a+next_w][b-next_w]:
            visited[a+next_w][b-next_w] = True
            queue.append((a+next_w, b-next_w, c))
    if a > 0 and z - c > 0: # A->C
        next_w = min(a, z-c)
        if not visited[a-next_w][b]:
            visited[a-next_w][b] = True
            queue.append((a-next_w, b, c+next_w))
    if b > 0 and z - c > 0: # B->C
        next_w = min(b, z-c)
        if not visited[a][b-next_w]:
            visited[a][b-next_w] = True
            queue.append((a, b-next_w, c+next_w))
    if c > 0 and x - a > 0: # C->A
        next_w = min(c, x-a)
        if not visited[a+next_w][b]:
            visited[a+next_w][b] = True
            queue.append((a+next_w, b, c-next_w))
    if c > 0 and y - b > 0: # C->B
        next_w = min(c, y-b)
        if not visited[a][b+next_w]:
            visited[a][b+next_w] = True
            queue.append((a, b+next_w, c-next_w))

print(*sorted(result))