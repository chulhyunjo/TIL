import sys
input = sys.stdin.readline


def makeTree(idx):
    while idx != 0:
        tree[idx] = tree[idx*2] + tree[idx*2+1]
        idx -=1


def changeTree(idx, change):
    dif = change - tree[idx]
    while idx > 0:
        tree[idx] += dif
        idx //= 2


N, Q = map(int,input().split())
nums = list(map(int,input().split()))

tmp = N
treeHeight = 0
while tmp:
    treeHeight += 1
    tmp //= 2
treeLeftStart = pow(2, treeHeight) - 1
tree = [0] * pow(2, treeHeight+1)
for i in range(1,N+1):
    tree[treeLeftStart+i] = nums[i-1]
makeTree(treeLeftStart)

for _ in range(Q):
    x, y, a, b = map(int,input().split())
    if x > y:
        x, y = y, x
    sum1 = 0
    startIdx = treeLeftStart + x
    endIdx = treeLeftStart + y
    while endIdx >= startIdx:
        if startIdx % 2 == 1:
            sum1 += tree[startIdx]
            startIdx += 1
        if endIdx % 2 == 0:
            sum1 += tree[endIdx]
            endIdx -= 1
        startIdx //= 2
        endIdx //= 2
    changeTree(treeLeftStart+a, b)
    print(sum1)