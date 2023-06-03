from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    times = [0] + list(map(int,input().split()))

    graph = [[] for _ in range(N+1)]
    nums = [0] * (N+1)
    answer = [0] * (N+1)

    for _ in range(K):
        a, b = map(int,input().split())
        graph[a].append(b)
        nums[b] += 1

    W = int(input())
    queue = deque()
    for i in range(1, N+1):
        if nums[i] == 0:
            queue.append(i)
            answer[i] = times[i]

    while queue:
        num = queue.popleft()
        if num == W:
            print(answer[num])
            break

        for i in graph[num]:
            nums[i] -= 1
            answer[i] = max(answer[i], answer[num] + times[i])
            if nums[i] == 0:
                queue.append(i)
