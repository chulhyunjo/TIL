import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

graph.sort(key = lambda x: (x[0], x[1]))

for answer in graph:
    print(*answer)