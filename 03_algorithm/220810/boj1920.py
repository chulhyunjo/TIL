def search(numbers,s,e,target):
    while s <= e:
        middle = (s+e)//2
        if target == numbers[middle]:
            return True
        elif target < numbers[middle]:
            e = middle - 1
        elif target > numbers[middle]:
            s = middle + 1
    return False

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
findl = list(map(int,input().split()))
for i in findl:
    print(1 if search(arr, 0, n-1, i) else 0)
