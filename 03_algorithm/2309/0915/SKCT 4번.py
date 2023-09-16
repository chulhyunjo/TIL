from collections import deque

def solution(board):
    print(*board, sep='\n')

    def check(i):
        if i == len(alpha):
            return True
        else:
            if bfs(alpha[i]):
                sx, sy = start_position[alpha[i]]
                ex, ey = end_position[alpha[i]]
                if dfs(sx, sy, ex, ey, i):
                    return True
            else:
                return False

    def dfs(x, y, ex, ey, i):
        for m in range(4):
            dx, dy = move[m]
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or 5<=nx or 5<=ny: continue
            score_board[x][y] += score[m]
            score_board[nx][ny] += score[(m + 2) % 4]
            if visited[nx][ny]:
                if nx == ex and ny == ey:
                    if check(i + 1):
                        return True
                score_board[x][y] -= score[m]
                score_board[nx][ny] -= score[(m + 2) % 4]
                continue
            visited[nx][ny] = 1
            if dfs(nx, ny, ex, ey, i):
                return True
            visited[nx][ny] = 0
            score_board[x][y] -= score[m]
            score_board[nx][ny] -= score[(m + 2) % 4]


    def bfs(alpha):
        sx, sy = start_position[alpha]
        ex, ey = end_position[alpha]
        queue = deque(([(sx, sy)]))
        bfs_visited = [[0]*5 for _ in range(5)]
        bfs_visited[sx][sy] = 1
        while queue:
            x, y = queue.popleft()
            for m in range(4):
                dx, dy = move[m]
                nx, ny = x+dx, y+dy
                if 0 > nx or 0 > ny or 5 <= nx or 5 <= ny: continue
                if visited[nx][ny]:
                    if nx == ex and ny == ey:
                        return True
                    continue
                if bfs_visited[nx][ny]: continue
                bfs_visited[nx][ny] = 1
                queue.append((nx, ny))
        return False




    move = [(0,1),(1,0),(0,-1),(-1,0)]
    score = [1,2,3,4]
    score_board = [[0] * 5 for _ in range(5)]
    visited = [[0] * 5 for _ in range(5)]

    start_position = dict()
    end_position = dict()
    alpha = []
    for i in range(5):
        for j in range(5):
            if board[i][j] != '.':
                visited[i][j] = 1
                if not start_position.get(board[i][j], 0):
                    start_position[board[i][j]] = (i,j)
                    alpha.append(board[i][j])
                else:
                    end_position[board[i][j]] = (i,j)

    check(0)
    return score_board


if __name__ == "__main__":
    # board = [".....", ".....", "..a..", ".b.b.", "c.a.c"]
    # board = ["a...c", ".b..d", "..c..", "...bd", "....a"]
    # board = ["a....", "e.e..", "dc...", "..bca", ".d..b"]
    board = ["a...b", ".....", ".....", "....b", "....a"]

    print(*solution(board), sep='\n')