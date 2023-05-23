import sys
input = lambda: sys.stdin.readline().rstrip()

def makeTree():
    i = pow(2,treeHeight-1) -1
    while i != 1:
        treeMin[i] = min(treeMin[i],treeMin[i*2], treeMin[i*2+1])
        treeMax[i] = max(treeMax[i],treeMax[i*2], treeMax[i*2+1])
        i -= 1


N, M = map(int, input().split())

treeHeight = 1
nums = N
while nums>0:
    treeHeight += 1
    nums //= 2
treeStartIndex = pow(2, treeHeight-1)
treeMin = [1000000000] * pow(2, treeHeight)
treeMax = [0] * pow(2, treeHeight)

for i in range(N):
    number = int(input())
    treeMin[treeStartIndex+i] = number
    treeMax[treeStartIndex+i] = number
makeTree()

for _ in range(M):
    a, b = map(int,input().split())

    startIdx = a + treeStartIndex-1
    endIdx = b + treeStartIndex-1
    min_answer = 1000000000
    max_answer = 0
    while endIdx >= startIdx:
        if startIdx % 2 == 1:
            min_answer = min(min_answer, treeMin[startIdx])
            max_answer = max(max_answer, treeMax[startIdx])
        if endIdx % 2 == 0:
            min_answer = min(min_answer, treeMin[endIdx])
            max_answer = max(max_answer, treeMax[endIdx])
        startIdx = (startIdx+1) // 2
        endIdx = (endIdx-1) // 2
    print(min_answer, max_answer)