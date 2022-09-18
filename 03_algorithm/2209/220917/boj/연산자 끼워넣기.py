import sys
sys.setrecursionlimit(10**5)
def math_(s, idx, p, mi, mul, div):
    global minV, maxV
    if p == mi == mul == div == 0:  # 연산을 다 했다면
        minV = min(s, minV)
        maxV = max(s, maxV)
        return
    if p > 0:   # 더하기가 남아 있다면 더하기
        math_(s + num[idx], idx + 1, p - 1, mi, mul, div)
    if mi > 0:  # 빼기
        math_(s - num[idx], idx + 1, p, mi - 1, mul, div)
    if mul > 0: # 곱하기
        math_(s * num[idx], idx + 1, p, mi, mul - 1, div)
    if div > 0: # 나누기
        if s < 0:   # 음수이면 양수로 바꾸고 나눠서 다시 음수로 바꾸기
            math_(-(-s // num[idx]), idx + 1, p, mi, mul, div - 1)
        else:       # 그냥 나누기
            math_(s // num[idx], idx + 1, p, mi, mul, div - 1)


n = int(input())
num = list(map(int, input().split()))
p, mi, mul, div = map(int, input().split())
minV = int(1e9) # 최대값
maxV = -int(1e9)    # 최소값
math_(num[0], 1, p, mi, mul, div)
print(maxV, minV, sep='\n')
