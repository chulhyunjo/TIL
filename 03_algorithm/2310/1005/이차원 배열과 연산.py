from collections import Counter
r, c, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(3)]

answer = -1
# N 행, M 열 개수
N = 3
M = 3
if r - 1 < N and c - 1 < M:
    if graph[r - 1][c - 1] == K:
        answer = 0

if answer == -1:
    for t in range(1,101):
        flag = 0
        newArr = []
        max_cnt = 0

        if N < M:
            graph = list(map(list, zip(*graph[::])))
            N, M = M, N
            flag = 1

        for i in range(N):
            nums = Counter(graph[i])
            del nums[0]
            max_cnt = max(len(nums.items())*2, max_cnt)
            arr = []
            for k, v in sorted(nums.items(), key = lambda x: (x[1], x[0])):
                arr += [k, v]
            newArr.append(arr)

        for i in range(N):
            newArr[i] += [0] * (max_cnt - len(newArr[i]))

        M = max_cnt
        if flag:
            graph = list(map(list, zip(*newArr[::])))
            N, M = M, N
        else:
            graph = newArr

        if r - 1 < N and c - 1 < M:
            if graph[r - 1][c - 1] == K:
                answer = t
                break

print(answer)