import sys
input = sys.stdin.readline


def makeTree(idx):
    while idx != 1:
        tree[idx//2] = tree[idx//2] * tree[idx] % 1000000007
        idx -= 1


def change(idx, change):
    tree[idx] = change
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx*2] % 1000000007 * tree[idx*2+1] % 1000000007


n, m, k = map(int,input().split())

treeHeight = 0
nums = n
while nums>0:
    treeHeight += 1
    nums //= 2

tree = [1] * (2**(treeHeight + 1))
treeLeftStart = 2**treeHeight-1
for i in range(1,n+1):
    tree[treeLeftStart+i] = int(input())
makeTree(2**(treeHeight+1) -1)

for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        change(treeLeftStart + b, c)
    else:
        startIdx = b + treeLeftStart
        endIdx = c + treeLeftStart
        answer = 1
        while endIdx >= startIdx:
            if startIdx % 2 == 1:
                answer = answer * tree[startIdx] % 1000000007
            if endIdx % 2 == 0:
                answer = answer * tree[endIdx] % 1000000007
            startIdx = (startIdx+1) // 2
            endIdx = (endIdx-1) // 2
        print(answer)