import sys
input = sys.stdin.readline

n = int(input())
plan = [list(map(int,input().rstrip().split())) for _ in range(n)]

plan = sorted(plan, key=lambda x: (x[1],x[0]))
result = 1
finish_time = plan[0][1]

for i in range(1,n):
    if plan[i][0] >= finish_time:
        finish_time = plan[i][1]
        result += 1

print(result)