def dfs(x):
    nxt_name = names[x]         # 현재 인덱스로 다음 사람 이름 찾기
    nxt_idx = idx[nxt_name]     # 다음 사람의 인덱스 찾기
    if not visited[nxt_idx]:
        visited[nxt_idx] = True
        dfs(nxt_idx)

T = 0
while True:
    T += 1
    N = int(input())
    if N == 0: break

    names = dict()
    idx = dict()

    for i in range(N):
        a, b = input().split()      # A -> B
        names[i] = b                # A의 인덱스 -> B의 이름
        idx[a] = i                  # 이름별 인덱스 저장

    visited = [False] *N            # 방문 확인
    answer = 0                      # 고리 개수
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer += 1
    print(T, answer)