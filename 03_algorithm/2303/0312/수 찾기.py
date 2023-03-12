n = int(input())
A = list(map(int,input().split()))
A.sort()
m = int(input())
B = list(map(int,input().split()))

for target in B:
    result = 0
    s = 0
    e = n-1
    while s <= e:
        mid = (s + e) // 2
        if target == A[mid]:
            result = 1
        if target > A[mid]:
            s = mid + 1
        else:
            e = mid - 1

    print(result)