import sys
input = sys.stdin.readline

def find(x):
    if nums[x] != x:
        nums[x] = find(nums[x])
        return nums[x]
    else:
        return x

def union(x,y):
    a = find(x)
    b = find(y)
    if a != b:
        nums[b] = a

n, m = map(int,input().rstrip().split())
nums = list(range(n+1))

for _ in range(m):
    status, a, b = map(int,input().rstrip().split())
    if status == 0:
        # union
        union(a,b)
    else:
        # find
        if (find(a) == find(b)):
            print('YES')
        else:
            print('NO')