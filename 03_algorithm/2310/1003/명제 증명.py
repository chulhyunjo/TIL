import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
graph = [[0] * 52 for _ in range(52)]

answer = 0
for _ in range(N):
    a, b = input().rstrip().split(' => ')
    if a == b:
        continue
    if not graph[ord(a) - 65 if ord(a) <= 90 else ord(a) - 71][ord(b) - 65 if ord(b) <= 90 else ord(b) - 71]:
        graph[ord(a) - 65 if ord(a) <= 90 else ord(a) - 71][ord(b) - 65 if ord(b) <= 90 else ord(b) - 71] = 1
        answer += 1

for i in range(52):
    graph[i][i] = 0

for k in range(52):
    for i in range(52):
        for j in range(52):
            if i != j and not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                answer += 1

print(answer)
for i in range(52):
    for j in range(52):
        if graph[i][j]:
            print(chr(i+65 if i < 26 else i + 71)+' => '+chr(j+65 if j < 26 else j + 71))