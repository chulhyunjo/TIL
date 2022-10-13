def garodul(i):
    for c in range(N-1):
        if garo(i, [c]):
            return 1
    for c in range(N-1):
        for d in range(N-1):
            if garo(1, [c, d]):
                return 2
    for c in range(N-1):
        for d in range(N-1):
            for e in range(N-1):
                if garo(2, [c,d,e]):
                    return 3
    return 0

def garo(i, l):
    for h in range(H):
        if not arr[h][l[i]] and (not l[i] or not arr[h][l[i]-1]) and (l[i] == N-2 or not arr[h][l[i]+1]):
            arr[h][l[i]] = 1
            if i == 0 and check():
                return True
            if i > 0:
                if garo(i-1, l):
                    return True
            arr[h][l[i]] = 0
    return False

def check():
    for i in range(1, N+1):
        if not go(i, i):
            return False
    return True

def go(s, i):
    for h in range(H):
        if i-2 >= 0 and arr[h][i-2]:
            i -= 1
        elif i <= N-1 and arr[h][i-1]:
            i += 1
    return True if s == i else False

N, M, H = map(int, input().split())
arr = [[0] * (N-1) for _ in range(H)]
G = [0] * (N-1)
Li = []

for _ in range(M):
    h, n = map(int, input().split())
    arr[h-1][n-1] = 1
    G[n-1] += 1

for i in range(N-1):
    if G[i] % 2:
        Li.append(i)

L = len(Li)
if L > 3:
    print(-1)
elif check():
    print(0)
else:
    result = garodul(0)
    if result: print(result)
    else:
        print(-1)