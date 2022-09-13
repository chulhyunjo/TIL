'''
각행의 합을 구하고 그 중 최대값을 출력하시오...
3
1 2 3
4 5 6
7 8 9
'''

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

maxV = 0
for i in range(n):
    sum1 = 0
    for j in range(n):
        sum1 += arr[i][j]
    maxV = sum1 if sum1 > maxV else maxV

print(maxV)