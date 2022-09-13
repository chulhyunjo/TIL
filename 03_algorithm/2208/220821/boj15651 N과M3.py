N, M = map(int, input().split())
S = []


def dfs():  # dfs 함수 생성
    if len(S) == M:
        print(' '.join(map(str, S)))
        return

    for i in range(1, N + 1):
        S.append(i)
        dfs()
        S.pop()
dfs()
