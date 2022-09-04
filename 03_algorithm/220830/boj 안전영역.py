import sys
sys.setrecursionlimit(10**6)    # 재귀 반복 limit 설정
dx = [0,0,1,-1]                 # dx, dy 선언
dy = [1,-1,0,0]

# dfs함수 선언, (x,y): 좌표, val: 내린 비의 양
def dfs(x,y,val):
    visited[x][y] = True
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] >= val:
                dfs(nx,ny,val)


n = int(input())                # NxN 배열의 크기
graph = [list(map(int,input().split())) for _ in range(n)]
minV = min(map(min,*graph))     # 2중 배열내의 최소 값 minV
maxV = max(map(max,*graph))     # 2중 배열내의 최대 값 maxV
result = 0                      # 최종 결과 값

for v in range(minV, maxV+1):   # 비가 내린 양을 최소부터 최대까지 다 확인
    cnt = 0                     # 현재 안전 영역의 개수를 담을 변수
    visited = [[False] * n for _ in range(n)]   # 방문 리스트
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= v and not visited[i][j]:  # 비가 내린 양보다 크거나 같은 곳은 안전 지역으로 확인
                dfs(i,j,v)      # i,j : 현재 좌표값, v: 안전지역의 기준값
                cnt += 1
    result = max(result, cnt)   # 안전 지역의 개수 최대값이 최종 결과값

print(result)