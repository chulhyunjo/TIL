import sys
input = sys.stdin.readline

N = int(input())
graph = list()
link = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int,input().rstrip().split())
    graph.append((a,b))
    link[a] += 1
    link[b] += 1

D = 0
G = 0
for q in range(1,N+1):
    if link[q] >= 3:
        G += (link[q] * (link[q]-1) * (link[q]-2) // 6)
for x, y in graph:
    D += (link[x]-1) * (link[y]-1)
if D > G*3:
    print('D')
if D < G*3:
    print('G')
if D == G*3:
    print('DUDUDUNGA')