N, L = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

def check(n):
    visited = [0] * N
    for i in range(N-1):
        flag = 0
        if graph[n][i] == graph[n][i+1]:continue
        if abs(graph[n][i] - graph[n][i+1]) > 1:
            return False
        cnt = 0
        if graph[n][i] > graph[n][i+1]:
            for j in range(i+1, N if i+1+L >= N else i + 1 + L):
                if visited[j]:
                    flag = 2
                    break
                if graph[n][j] == graph[n][i+1]:
                    flag = 1
                    cnt += 1
                else:
                    flag = 2
                    break

        elif graph[n][i] < graph[n][i+1]:
            for j in range(i, -1 if i - L <= -1 else i - L, -1):
                if visited[j]:
                    flag = 2
                    break
                if graph[n][j] == graph[n][i]:
                    cnt += 1
                else:
                    flag = 2
                    break
        if flag == 2:
            return False
        if cnt == L:
            if flag==1:
                for j in range(i+1, i+1+L):
                    visited[j] = 1
            else:
                for j in range(i, i-L, -1):
                    visited[j] = 1
        else:
            return False
    return True


answer = 0
for i in range(N):
    if check(i):
        answer += 1
graph = list(map(list, zip(*graph[::])))

for i in range(N):
    if check(i):
        answer += 1

print(answer)