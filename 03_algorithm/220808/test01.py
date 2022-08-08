'''
입력
9
7 4 2 0 0 6 0 7 0
'''

n = int(input())
arr = list(map(int, input().split()))
maxV = arr[0] # 첫원소를 최대값으로 가정

for i in range(1, n): # 나머지 모든 원소에 대해
    if arr[i] > maxV:
        maxV = arr[i]