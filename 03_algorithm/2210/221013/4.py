def position(n, i):
    global result, max_result
    if n == 0:
        result = 0
        game(E)
        max_result = result if result > max_result else max_result
        return
    if i == M:
        return
    else:
        for j in range(i, M):
            A.append([N, j])
            position(n-1, j+1)
            A.pop()

def game(el):
    global result
    K = set()
    for ay, ax in A:
        T = []
        for ey, ex in el:
            d = abs(ay-ey)+abs(ax-ex)
            if d <= D:
                T.append((d, ex, ey))
        if T:
            K.add(sorted(T)[0][1:])
    result += len(K)
    KE = []
    for k in K:
        KE.append([k[1], k[0]])
    NE = []
    for e in el:
        if e in KE or e[0] == N-1:
            pass
        else:
            NE.append([e[0]+1, e[1]])
    if NE:
        game(NE)

N, M, D = map(int, input().split())
arr = []
E = []
A =[]
result = 0
max_result = 0
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j]:
            E.append([i, j])
    arr.append(line)
position(3, 0)
print(max_result)

