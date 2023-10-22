import sys
input = sys.stdin.readline

for _ in range(int(input())):
    W = input().rstrip()
    K = int(input())

    alp = dict()
    for i in range(len(W)):
        alp[W[i]] = alp.get(W[i], []) + [i]

    minV = 10001
    maxV = 0
    for V in alp.values():
        l = len(V)
        if l >= K:
            for i in range(l-K+1):
                minV = min(V[i+K-1] - V[i] + 1, minV)
                maxV = max(V[i+K-1] - V[i] + 1, maxV)

    if maxV:
        print(minV, maxV)
    else:
        print(-1)

