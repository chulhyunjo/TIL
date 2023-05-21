import sys
input = sys.stdin.readline

def addTree(idx):
    left = right = 0
    if idx * 2 < (2**(q+1)):
        left = addTree(2*idx)
    if idx * 2 + 1 < (2**(q+1)):
        right = addTree(2*idx+1)
    if left or right:
        tree[idx] = right + left
        return tree[idx]
    else:
        return tree[idx]

def makeTree(idx, change):
    diff = change - tree[idx]
    while idx > 0:
        tree[idx] += diff
        idx //= 2

n, m, k = map(int,input().split())

q = 0
while 2**q < n:
    q += 1

tree = [0 for _ in range(2**(q+1)+1)]
for i in range(n):
    tree[2**q+i] = int(input())
addTree(1)

for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        makeTree((2**q-1)+b, c)
    else:
        start_idx = b + (2**q-1)
        end_idx = c + (2**q-1)
        sum1 = 0
        while end_idx >= start_idx:
            if start_idx % 2 == 1:
                sum1 += tree[start_idx]
            if end_idx % 2 == 0:
                sum1 += tree[end_idx]
            start_idx = (start_idx + 1) // 2
            end_idx = (end_idx - 1) // 2
        print(sum1)