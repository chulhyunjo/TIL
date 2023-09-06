import sys
input = sys.stdin.readline

N = int(input())
days = []

start, end = 365, 0
for _ in range(N):
    s, e = map(int,input().split())
    if s < start:
        start = s
    if end < e:
        end = e
    days.append((s,e))

graph = [0] * (end - start + 1)

for s, e in days:
    for i in range(s, e+1):
        graph[i-start] += 1

cnt = 0
max_num = 0
area = 0
for i in range(end - start + 1):
    if graph[i] > 0:
        cnt += 1
        max_num = max(max_num, graph[i])
    else:
        area += cnt * max_num
        cnt = max_num = 0
if cnt:
    area += cnt * max_num
print(area)