target = int(input())
n = int(input())
numsT = [True] * 10
if n != 0:
    b = list(map(int,input().split()))
    for i in b:
        numsT[i] = False

result = abs(100 - target)
for j in range(1000000):
    avNum = True
    for k in str(j):
        if not numsT[int(k)]:
            avNum = False
            break

    if avNum:
        result = min(result, abs(j - target)+len(str(j)))

print(result)