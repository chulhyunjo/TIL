def dfs(start):                         # dfs 함수 선언
    visited[start] = True               # 현재 위치를 방문
    check_move.append(start)            # 이동한 경로를 담을 check_move 리스트에 위치 담기
    for i in graph[start]:              # 현재 위치에서 이동할 수 있는 위치 전체 탐색
        if not visited[i]:              # 만약 방문하지 않았다면 방문하기
            dfs(i)


for tc in range(1, int(input())+1):     # 테스트 케이스 개수 입력
    v, e = map(int,input().split())     # v: 노드의 개수, e: 간선의 개수
    graph = [[] for _ in range(v+1)]    # 이어진 노드들을 graph에 담기ㅣ
    visited = [False] * (v+1)           # 방문했는지 확인하기 위한 리스트

    for _ in range(e):                  # e개의 간선 입력하기위해 range(e)
        a, b = map(int,input().split()) # a: 출발지, b: 도착지
        graph[a].append(b)              # a<->b가 아닌 a ->로 이어지기 떄문에 하나만 담기

    check_move = []                     # 이동한 동선을 담을 check_move 선언
    s, g = map(int,input().split())     # s: 출발 노드, g: 도착노드

    dfs(s)                              # dfs 함수를 선언해서 s->g로 이동한 동선 탐색

    result = 1 if g in check_move else 0    # s->g로 가는 노선이 있으면 1 없으면 0
    print(f'#{tc} {result}')