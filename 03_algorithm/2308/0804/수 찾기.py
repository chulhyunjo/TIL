N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

M = int(input())
find = list(map(int,input().split()))

for i in find:
    s = 0
    e = N-1
    find = 0
    while s <= e:
        mid = (s+e) // 2

        if numbers[mid] == i:
            find = 1
            break

        elif numbers[mid] > i:
            e = mid - 1

        else:
            s = mid + 1

    if find:
        print(1)
    else:
        print(0)