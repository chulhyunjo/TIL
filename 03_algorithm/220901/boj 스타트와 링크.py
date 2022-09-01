from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]
nums = list(range(n))
result = 1000
for i in combinations(nums,n//2):
    not_list = [x for x in nums if x not in i]
    sum1 = 0
    sum2 = 0
    for x1 in i:
        for y1 in i:
            sum1 += graph[x1][y1]

    for x2 in not_list:
        for y2 in not_list:
            sum2 += graph[x2][y2]

    result = min(result , abs(sum1-sum2))

print(result)