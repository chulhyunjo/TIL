import sys
input = sys.stdin.readline

def moveFire():
    moveTo = dict()
    for k, v in fireball.items():
        r, c = k
        for m, s, d in v:
            dr, dc = D[d]
            nr, nc = r + dr*s, c + dc*s
            nr, nc = nr % N, nc % N
            nr = N+nr if nr<=0 else nr
            nc = N+nc if nc<=0 else nc
            moveTo[(nr,nc)] = moveTo.get((nr,nc), []) + [(m, s, d)]
    return moveTo

def div():
    delete = []
    for k, v in fireball.items():
        length = len(v)
        if length == 1 :continue
        sum_m = 0
        sum_s = 0
        flag = 0
        for m, s, d in v:
            sum_m += m
            sum_s += s
            flag += d%2
        nm = sum_m // 5
        ns = sum_s // length
        if nm > 0:
            if flag == 0 or flag == length:
                fireball[k] = [(nm,ns,0), (nm,ns,2), (nm,ns,4), (nm,ns,6)]
            else:
                fireball[k] = [(nm, ns, 1), (nm, ns, 3), (nm, ns, 5), (nm, ns, 7)]
        else:
            delete.append(k)

    for x, y in delete:
        del fireball[(x,y)]


D = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
N, M, K = map(int,input().split())
fireball = dict()

for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    fireball[(r,c)] = [(m, s,d)]

for _ in range(K):
    fireball = moveFire()
    div()

answer = 0
for v in fireball.values():
    for m, s, d in v:
        answer += m
print(answer)