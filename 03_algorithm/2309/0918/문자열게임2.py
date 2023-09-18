from collections import deque
T = int(input())
for _ in range(T):      # T =100
    W = input()
    N = len(W)          # 1<=N<=10000
    K = int(input())    # 1 <= K <= 10000
    if K == 1:
        print(1,1)
    else:
        alpha = dict()
        min_answer = N
        max_answer = -1
        for i in range(N):
            now = alpha.get(W[i], [0,deque()])
            now[1].append(i)
            now[0] += 1
            if now[0] == K:
                length = now[1][-1] - now[1][0] + 1
                min_answer = min(length, min_answer)
                max_answer = max(length, max_answer)
                now[1].popleft()
                now[0] -= 1
            alpha[W[i]] = [now[0], now[1]]
        if max_answer == -1:
            print(-1)
        else:
            print(min_answer, max_answer)
