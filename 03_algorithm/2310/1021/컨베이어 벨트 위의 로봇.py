from collections import deque

N, K = map(int,input().split())
cnt = 0
belt = deque(list(map(int,input().split())))
robots = deque([0] * N)

answer = 0
while cnt < K:
    answer += 1
    belt.appendleft(belt.pop())
    robots[-1] = 0
    robots.appendleft(robots.pop())
    robots[-1] = 0

    for i in range(N-1, -1, -1):
        if robots[i] and belt[i+1] != 0:
            if robots[i+1]: continue
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
            robots[i+1], robots[i] = robots[i], 0

    if not robots[0] and belt[0]:
        robots[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1


print(answer)