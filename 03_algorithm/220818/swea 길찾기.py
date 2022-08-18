def dfs(start):                             # dfs 함수 생성
    visited[start] = True                   # 이동한 칸 방문
    move.append(start)                      # 이동한 칸을 담은 리스트에 현재 칸 삽입
    for i in graph[start]:                  # 다음 이동할 칸 탐색
        if not visited[i]:                  # 방문하지 않았으면 방문하기
            dfs(i)

for _ in range(10):
    t, n = map(int,input().split())         # t: 현재 테스트케이스, n:루트 개수
    arr = list(map(int,input().split()))    # 루트를 담은 리스트
    graph = [[] for _ in range(100)]        # 이동할 수 있는 칸을 담은 리스트
    for i in range(0,2*n,2):                # 루트를 담기위한 for문
        a, b = arr[i], arr[i+1]
        graph[a].append(b)

    move = []                               # 이동한 칸을 담을 변수
    visited = [False] * 100                 # 방문한지 안한지 담을 리스트
    result = 0                              # 결과값 있으면 '1' 없으면 '0'
    dfs(0)                                  # dfs탐색 시작

    if 99 in move:                          # 마지막 칸 99으로 이동 할 수 있으면 '1'
        result = 1
    print(f'#{t} {result}')