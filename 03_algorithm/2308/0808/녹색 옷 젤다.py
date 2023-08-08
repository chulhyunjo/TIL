import heapq
import sys
input = sys.stdin.readline
INF = 125*125*9 + 1

def bfs():
    # [1] 최소 힙을 이용해서 최소 값부터 확인
    visited[0][0] = graph[0][0]
    pq = [(visited[0][0], 0, 0)]

    # bfs
    while pq:
        # [2] now: 현재 잃은 루피 개수, (x, y): 좌표
        now, x, y = heapq.heappop(pq)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
            # 범위에서 벗어나면 continue
            if 0 > nx or N <= nx or 0 > ny or N <= ny: continue
            # 다음 이동하는 칸의 최소값이 작거나 같으면 확인X(continue)
            if visited[nx][ny] <= now + graph[nx][ny]: continue
            visited[nx][ny] = now + graph[nx][ny]
            # [N-1][N-1] 최종 목적지에 도달하면 return
            if nx == N-1 and ny == N-1:
                return visited[N-1][N-1]
            # 다음 칸에 대한 정보를 heap에 저장
            heapq.heappush(pq, (visited[nx][ny], nx, ny))

T = 1
while True:
    N = int(input())
    if N == 0: break

    graph = [list(map(int,input().split())) for _ in range(N)]

    # 각 노드까지 이동할 때 잃는 최소 금액
    visited = [[INF] * N for _ in range(N)]

    answer = bfs()
    print(f'Problem {T}: {answer}')
    T += 1