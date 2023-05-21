import sys
input = sys.stdin.readline
noNode = 10**9+1
def makeTree(idx):
    maxIdx = 2**(treeHeight+1)
    left = right = noNode
    if idx*2 < maxIdx:
        left = makeTree(idx*2)
    if idx*2+1 < maxIdx:
        right = makeTree(idx*2+1)
    tree[idx] = min(left, right, tree[idx])
    return tree[idx]

n, m = map(int,input().split())

treeHeight = 0
nums = n

while nums>0:
    treeHeight += 1
    nums //= 2
treeLeftStart = (2**treeHeight)

tree = [noNode] * (2**(treeHeight+1))

for i in range(n):
    tree[treeLeftStart+i] = int(input())
makeTree(1)

for _ in range(m):
    a, b = map(int,input().split())
    start_idx = a + (treeLeftStart-1)
    end_idx = b + (treeLeftStart -1)
    answer = noNode
    while end_idx>=start_idx:
        if start_idx % 2 == 1:
            answer = min(answer, tree[start_idx])
        if end_idx % 2 == 0:
            answer = min(answer, tree[end_idx])
        start_idx = (start_idx + 1) //2
        end_idx = (end_idx - 1) // 2
    print(answer)
