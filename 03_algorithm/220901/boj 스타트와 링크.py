from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input().rstrip())       # NxN 배열
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]
nums = list(range(n))           # 0~n-1까지 리스트로 만들기
result = 1000                   # 최소값을 담을 변수선언, 4<=N<=20이고 수는 100보다 작으므로 최대값은 1000이다
for i in combinations(nums,n//2):   # 절반 만큼 combinattion 돌리기 (부분 집합)
    not_list = [x for x in nums if x not in i]  # 위의 combinations에 포함되지 않는 수들을 not_list에 담기
    sum1 = 0                    # combinations의 총합을 담을 sum1
    sum2 = 0                    # combinations 외의 나머지 총합을 담을 sum2
    for x1 in i:
        for y1 in i:
            sum1 += graph[x1][y1]   # x1 == y1일때 무조건 0이므로 그냥 다 더했다.

    for x2 in not_list:             # 위와 같다
        for y2 in not_list:
            sum2 += graph[x2][y2]

    result = min(result , abs(sum1-sum2)) # sum1, sum2의 차이가 가장 적을때가 result

print(result)