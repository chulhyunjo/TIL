"""
11
1 14
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 12
0 14
"""
import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().rstrip().split())) for _ in range(N)]

times.sort(key = lambda x: (x[1], x[0]))

result = 0
endTime = -1

for a, b in times:
    if endTime <= a:
        result += 1
        endTime = b
print(result)