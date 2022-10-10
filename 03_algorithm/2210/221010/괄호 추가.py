def calculate(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def check(d, pre):
    global maxV
    if d >= n:
        maxV = max(maxV, pre)
        return
    check(d+2, calculate(pre,int(num[d+1]),num[d]))
    if d+3<n:
        check(d+4, calculate(pre,calculate(int(num[d+1]),int(num[d+3]),num[d+2]),num[d]))

n = int(input())
num = list(input())
maxV = -(2**31)
check(1,int(num[0]))
print(maxV)