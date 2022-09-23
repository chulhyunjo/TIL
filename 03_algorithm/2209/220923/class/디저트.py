dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(x,y,move,cnt,cnt2,ob):
    global eat_set, move_cnt, startX, startY
    eat_set.add(graph[x][y])
    if move_cnt == cnt:
        move += 1
        move_cnt = 0
    if (move == 0 or move == 2) and move_cnt == cnt2 and ob == 1:
        move += 1
        move_cnt = 0
    if move == 1 and move_cnt == cnt2 and ob == 2:
        move += 1
        move_cnt = 0
    if move == 4 : return 0
    nx, ny = x+dx[move], y + dy[move]

    if (nx, ny) == (startX, startY) and move == 3: return 1
    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] in eat_set : return 0
        move_cnt += 1
        if dfs(nx,ny,move,cnt,cnt2,ob):
            return 1
    else:
        move = move+1
        move_cnt = 0
        if dfs(x,y,move,cnt,cnt2,ob): return 1


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = -1
    for i in range(1,n//2):
        for m in range(1,i+1):
            for j in range(n):
                for k in range(n):
                    startX, startY = j,k
                    eat_set = set()
                    move_cnt = 0
                    r1 = dfs(j,k,0,i,m,1)
                    if r1:
                        eat_sum = len(eat_set)
                        result = eat_sum if eat_sum > result else result
                    eat_set = set()
                    move_cnt = 0
                    r2 = dfs(j,k,0,i,m,2)
                    if r2:
                        eat_sum = len(eat_set)
                        result = eat_sum if eat_sum > result else result
    print(result)