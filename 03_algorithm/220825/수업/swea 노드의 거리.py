for tc in range(1, int(input())+1):
    v, e = map(int,input().split())         # v : 노드 개수, e : 간선 개수
    graph = [[] for _ in range(v+1)]        # 이동경로 담기
    for _ in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    s, g = map(int,input().split())         # s: 시작, g: 도착

    queue = [(s, 0)]                        # 큐에 (시작점, 이동횟수)담기
    visited = [False] * (v+1)               # 방문 목록
    result = 0                              # 결과값
    while queue:                            # 이동 경로 있는 동안 실행
        s, cnt = queue.pop(0)
        visited[s] = True                   # 현재 노드 방문 기록

        for i in graph[s]:
            if not visited[i]:
                queue.append((i, cnt + 1))  # 다음 노드, 이동횟수 담기
            if i == g:                      # 도착 지점이면
                result = cnt + 1            # 이동횟수 결과값에 담기
        if result:                          # 도착 지점에 방문했다면
            break                           # break

    print(f'#{tc} {result}')