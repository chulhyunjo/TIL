def changeBlank(x, y):
    for dx, dy in [(1,0),(0,-1),(0,1),(-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
        if blanks[nx][ny]:
            blanks[nx][ny] -= 1

def findLikes(x, y, likes):
    cnt = 0
    for dx, dy in [(1,0),(0,-1),(0,1),(-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
        if graph[nx][ny] in likes:
            cnt += 1
    return cnt

N = int(input())

# 앉은 자리
graph = [[0] * N for _ in range(N)]
# 빈칸 개수
blanks = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 or i == N-1:
            if j == 0 or j == N-1:
                blanks[i][j] = 2
            else:
                blanks[i][j] = 3
        else:
            if j == 0 or j == N-1:
                blanks[i][j] = 3
            else:
                blanks[i][j] = 4

# 좋아하는 사람
likes = dict()
order = [] # 앉는 순서
for _ in range(N**2):
    num, *like = map(int,input().split())
    likes[num] = like
    order.append(num)

# 앉은 사람의 위치
sitDown = dict()

# 한명씩 앉기
for num in order:
    flag = 0
    max_cnt = 0
    can_sit = []
    max_blank = -1
    for like in likes[num]:
        if sitDown.get(like, 0):
            i, j = sitDown[like]
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = i + dx, j + dy
                if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
                if graph[nx][ny]: continue
                cnt = findLikes(nx,ny, likes[num])
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_blank = blanks[nx][ny]
                    can_sit = [(nx,ny)]
                elif max_cnt == cnt:
                    if max_blank == blanks[nx][ny]:
                        can_sit.append((nx, ny))
                    elif max_blank < blanks[nx][ny]:
                        can_sit = [(nx, ny)]
                        max_blank = blanks[nx][ny]
    if can_sit:
        can_sit.sort()
        px, py = can_sit[0]
    else:
        px, py = -1, -1
        max_blank = -1
        for i in range(N):
            for j in range(N):
                if max_blank < blanks[i][j] and not graph[i][j]:
                    max_blank = blanks[i][j]
                    px, py = i, j

    blanks[px][py] = 0
    sitDown[num] = (px, py)
    graph[px][py] = num
    changeBlank(px, py)
answer = 0
for i in range(N):
    for j in range(N):
        cnt = findLikes(i, j, likes[graph[i][j]])
        if cnt == 0:
            answer += 0
        elif cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        else:
            answer += 1000
print(answer)