import sys
input = sys.stdin.readline

def makeTree(idx):
    if idx*2 < (2**treeHeight):
        makeTree(idx*2)
        tree[idx] += tree[idx*2]
    if idx*2+1 < (2**treeHeight):
        makeTree(idx*2+1)
        tree[idx] += tree[idx*2+1]


def changeNum(idx, diff):
    while idx>0:
        tree[idx] += diff
        idx //= 2


N, M, K = map(int,input().split())

treeHeight = 1
nums = N

while nums > 0:
    nums //= 2
    treeHeight += 1

treeLeftStart = (2**(treeHeight-1)) -1
tree = [0] * (2**treeHeight)

for i in range(1,N+1):
    tree[treeLeftStart+i] = int(input())
makeTree(1)

for _ in range(M+K):
    a, *nums = map(int,input().rstrip().split())
    if a == 1:
        s = nums[0]
        e = nums[1]
        change = nums[2]
        for i in range(s, e+1):
            changeNum(treeLeftStart+i, change)

    if a == 2:
        start_idx = nums[0] + treeLeftStart
        end_idx = nums[1] + treeLeftStart
        sum1 = 0
        while end_idx >= start_idx:
            if start_idx % 2 == 1:
                sum1 += tree[start_idx]
                start_idx += 1
            if end_idx % 2 == 0 :
                sum1 += tree[end_idx]
                end_idx -= 1
            start_idx //= 2
            end_idx //= 2
        print(sum1)