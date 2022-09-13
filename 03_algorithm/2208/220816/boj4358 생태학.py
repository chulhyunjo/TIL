import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for _ in range(m):

    i,j = map(int,input().split())
    check = arr[i-1:j]
    if check == check[::-1]:
        print(1)
    else:
        print(0)