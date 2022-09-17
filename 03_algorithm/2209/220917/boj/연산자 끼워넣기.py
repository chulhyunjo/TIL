import sys
sys.setrecursionlimit(10**5)
def math_(s, idx, p, mi, mul, div):
    global minV, maxV
    if p == mi == mul == div == 0:
        minV = min(s, minV)
        maxV = max(s, maxV)
        return
    if p > 0:
        math_(s + num[idx], idx + 1, p - 1, mi, mul, div)
    if mi > 0:
        math_(s - num[idx], idx + 1, p, mi - 1, mul, div)
    if mul > 0:
        math_(s * num[idx], idx + 1, p, mi, mul - 1, div)
    if div > 0:
        if s < 0:
            math_(-(-s // num[idx]), idx + 1, p, mi, mul, div - 1)
        else:
            math_(s // num[idx], idx + 1, p, mi, mul, div - 1)


n = int(input())
num = list(map(int, input().split()))
p, mi, mul, div = map(int, input().split())
minV = int(1e9)
maxV = -int(1e9)
math_(num[0], 1, p, mi, mul, div)
print(maxV, minV, sep='\n')
