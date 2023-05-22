def findNumber(n):
    start = 0
    end = N-1
    while end>=start:
        middle = (start + end) // 2
        if numbers[middle] == n:
            return True

        if numbers[middle] > n:
            end = middle - 1

        if numbers[middle] < n:
            start = middle + 1
    return False

N = int(input())
numbers = sorted(list(map(int,input().split())))
M = int(input())
findNumbers = list(map(int,input().split()))

for i in findNumbers:
    if findNumber(i):
        print(1)
    else:
        print(0)