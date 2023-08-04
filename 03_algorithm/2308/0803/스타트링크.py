from collections import deque
# F층으로 이루어짐
# G 스타트링크가 있는 자리
# S 강호가 있는 위치 -> G로 이동
# U, D 만큼 위 아래 이동
def bfs():
    while queue:
        x = queue.popleft()
        if x - D == G or x + U == G:
            return moves[x] + 1

        if x + U <= F and not visited[x + U]:
            queue.append(x+U)
            visited[x+U] = True
            moves[x+U] = moves[x] + 1

        if x - D > 0 and not visited[x - D]:
            queue.append(x-D)
            visited[x-D] = True
            moves[x-D] = moves[x] + 1

    return -1

F, S, G, U, D = map(int,input().split())
if S == G:
    print(0)
elif S > G and D == 0:
    print('use the stairs')
elif S < G and U == 0:
    print('use the stairs')
else:
    moves = [-1] * (F+1)
    visited = [False] * (F+1)
    visited[S] = True
    moves[S] = 0
    queue = deque([S])

    ans = bfs()
    if ans != -1:
        print(ans)
    else:
        print('use the stairs')