def dfs(depth,sum1):
    global result           # 최소값을 담을 변수
    if sum1 > result:       # 이미 최소값을 넘었을 경우 더이상 실행 x
        return

    if depth == n:          # 깊이가 마지막일 때
        if sum1 < result:   # 현재 합이 result 보다 작으면
            result = sum1   # result 초기화
        return
    else:
        for j in range(n):  # 1 ~ n 행 까지
            if not visited[j]:  # 방문하지 않은 열인 경우
                visited[j] = True   # 방문한 열로 교체
                dfs(depth+1, sum1 + graph[depth][j]) # 다음 깊이 탐색, sum1에 저장
                visited[j] = False  # 방문하지 않은 열로 바꾸기, 다음 탐색을 위해


for tc in range(1,int(input())+1):
    n = int(input())                # nxn 배열 크기 선언
    graph = [list(map(int, input().split())) for _ in range(n)] # nxn배열 선언
    result = 100                    # 합의 최소값을 받을 변수 선언
    visited = [False] * n           # 같은 열을 담으면 안되므로 visited리스트 선언
    dfs(0, 0)                       # dfs(깊이, 합)
    print(f'#{tc} {result}')