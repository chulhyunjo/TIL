def solution(points, routes):
    N = len(points)
    M = len(routes[0])
    X = len(routes)
    position = dict()
    graph = dict()

    for i in range(X):
        x, y = points[routes[i][0] - 1]
        graph[(x-1, y-1)] = graph.get((x-1, y-1), 0) + 1
        position[i] = (x-1, y-1)

    # 중첩된 곳 확인
    answer = 0
    for v in graph.values():
        if v > 1:
            answer += 1

    # 인덱스별 이동경로
    moves = [1] * X
    while graph:
        for i in range(X):
            if position.get(i, -1) == -1: continue # 종료됐으면 끝
            now_x, now_y = position[i]

            # 종료되었다면 삭제
            if moves[i] == M:
                if graph[(now_x, now_y)] == 1:
                    del graph[(now_x, now_y)]
                else:
                    graph[(now_x, now_y)] -= 1
                del position[i]
                continue

            # 다음 이동 위치
            nxt_x, nxt_y = list(map(lambda x: x-1, points[routes[i][moves[i]]-1]))
            if graph[(now_x, now_y)] == 1:
                del graph[(now_x, now_y)]
            else:
                graph[(now_x, now_y)] -= 1

            if nxt_x != now_x:
                if nxt_x > now_x:
                    now_x += 1
                else:
                    now_x -= 1
            else:
                if nxt_y > now_y:
                    now_y += 1
                else:
                    now_y -= 1

            if now_x == nxt_x and now_y == nxt_y:
                moves[i] += 1

            graph[(now_x, now_y)] = graph.get((now_x, now_y), 0) + 1
            position[i] = (now_x, now_y)

        for v in graph.values():
            if v > 1:
                answer += 1

    return answer
