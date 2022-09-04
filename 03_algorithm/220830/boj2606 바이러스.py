def dfs(v):
    global cnt              # 바이러스 걸리는 컴퓨터의 수
    visited[v] = True       # 현재 컴퓨터 방문
    for q in graph[v]:      # 다음 지점 확인
        if not visited[q]:  # 방문하지 않았으면 이동
            cnt += 1        # 바이러스 개수 + 1
            dfs(q)


v = int(input())            # v: 컴퓨터의 수
e = int(input())            # e: 연결 되어 컴퓨터 쌍의 수
graph = [[] for _ in range(v+1)]
for _ in range(e):          # 연결된 컴퓨터들을 리스트에 담기
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (v+1)   # 방문 리스트
cnt = 0                     # 바이러스 걸리는 컴퓨터의 수 담을 변수 선언
dfs(1)                      # 1번 컴퓨터 기준으로 몇개 걸리는지 확인해야 함으로 dfs(1)
print(cnt)                  # 결과값 출력