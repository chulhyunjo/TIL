import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs 함수
def dfs(v):
    visited[v] = True       # 현재 지점 방문
    for q in graph[v]:      # 다음 이동 지점 찾기
        if not visited[q]:  # 방문하지 않았으면 이동
            dfs(q)

n, m = map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):          # 각 정점별로 이동할 수 있는 노드 담기
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0                  # 결과 값을 담을 변수
visited = [False] * (n+1)   # 방문 리스트
for i in range(1,n+1):      # 1 ~ n 까지 전체확인
    if not visited[i]:      # 방문하지 않았으면 dfs실행
        dfs(i)
        result += 1
# 출력
print(result)