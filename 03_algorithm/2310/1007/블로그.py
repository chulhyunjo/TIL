N, M = map(int,input().split())
visited = list(map(int,input().split()))
if sum(visited) == 0:
    print('SAD')
else:
    max_visit = sum(visited[:M])
    visit_cnt = max_visit
    cnt = 1

    for i in range(M, N):
        visit_cnt += visited[i] - visited[i-M]
        if visit_cnt > max_visit:
            max_visit = visit_cnt
            cnt = 1
        elif visit_cnt == max_visit:
            cnt += 1
    
    print(max_visit)
    print(cnt)