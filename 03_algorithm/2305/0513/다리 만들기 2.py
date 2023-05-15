from collections import deque
import heapq
dx, dy = [0,1,-1,0], [1,0,0,-1]

# 땅 만들기
def makeGround(x,y,nums):
    graph[x][y] = nums
    visited[x][y] = True
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or N <= nx or M <= ny or visited[nx][ny]: continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = nums
                visited[nx][ny] = True
                queue.append((nx,ny))


def findBridge(x, y, status, startGroundNum):
    nx = x + dx[status]
    ny = y + dy[status]
    cnt = 0
    while 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] != 0:
            if cnt >=2:
                heapq.heappush(pq, (cnt, startGroundNum, graph[nx][ny]))
            break
        nx += dx[status]
        ny += dy[status]
        cnt += 1

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x
        return True
    else:
        return False

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
pq = []

# 땅 구분하기
nums = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            makeGround(i, j, nums)
            nums += 1
parents = list(range(nums))


for i in range(N):
    for j in range(M):
        for k in range(2):
            ni, nj = i+dx[k], j+dy[k]
            if 0 > ni or 0 > nj or N<=ni or M<=nj: continue
            if graph[ni][nj] == 0 and graph[i][j] != 0:
                findBridge(i,j,k, graph[i][j])

nodes = 0
answer = 0
while nodes < nums-2 and pq:
    dis, s, e = heapq.heappop(pq)
    if union(s, e):
        answer += dis
        nodes += 1

if nodes == nums-2:
    print(answer)
else:
    print(-1)

