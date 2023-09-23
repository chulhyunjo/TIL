from collections import deque

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DW = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def not_in_graph(x, y):
    return 0 > x or N <= x or 0 > y or N <= y


N, M, K, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]  # 박멸제가 뿌려져 있는지 확인


# 번식
def grow():
    growing = dict()
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                cnt = 0  # 근접한 나무 개수
                for dx, dy in D:
                    nx, ny = i + dx, j + dy
                    if not_in_graph(nx, ny): continue
                    if graph[nx][ny] > 0:
                        cnt += 1
                if cnt:
                    growing[(i, j)] = cnt
    if growing:
        for k, v in growing.items():
            x, y = k
            graph[x][y] += v


# 양 옆으로 확산
def spread():
    spreading = dict()
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                position = []
                cnt = 0  # 번식 가능한 칸
                for dx, dy in D:
                    nx, ny = i + dx, j + dy
                    if not_in_graph(nx, ny): continue
                    if graph[nx][ny] == 0 and not visited[nx][ny]:  # 박멸제가 없고 빈칸인 경우
                        cnt += 1
                        position.append((nx, ny))

                for x, y in position:
                    spreading[(x, y)] = spreading.get((x, y), 0) + (graph[i][j] // cnt)

    for k, v in spreading.items():
        x, y = k
        graph[x][y] = v


def findBest(time):
    global answer
    best = 0  # 가장 많은 개수
    position_x, position_y = 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] in [0, -1]: continue
            cnt = graph[i][j]
            for dx, dy in DW:
                cnt2 = 0
                nx, ny = i + dx, j + dy
                while not not_in_graph(nx, ny) and not graph[nx][ny] in [0, -1] and cnt2 < K:
                    cnt += graph[nx][ny]
                    nx, ny = nx + dx, ny + dy
                    cnt2 += 1

            if cnt > best:
                best = cnt
                position_x, position_y = i, j

    graph[position_x][position_y] = 0
    visited[position_x][position_y] = time + C + 1
    answer += best

    for dx, dy in DW:
        nx, ny = position_x + dx, position_y + dy
        cnt2 = 0
        while not not_in_graph(nx, ny) and graph[nx][ny] != -1 and cnt2 < K:
            visited[nx][ny] = time + C + 1
            if graph[nx][ny] == 0:
                break
            graph[nx][ny] = 0
            nx, ny = nx + dx, ny + dy
            cnt2 += 1


def changeVisit(time):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == time:
                visited[i][j] = 0


answer = 0
for t in range(1, M + 1):
    changeVisit(t)

    grow()

    spread()

    findBest(t)

print(answer)