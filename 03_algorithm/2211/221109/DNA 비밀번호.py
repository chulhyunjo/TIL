def check(alpha):
    if alpha == 'A':
        idx = 0
    elif alpha == 'C':
        idx = 1
    elif alpha == 'G':
        idx = 2
    elif alpha == 'T':
        idx = 3
    return idx

def check2():
    for i in range(4):
        if num[i] > now[i]:
            return False
    return True

n, m = map(int,input().split())
DNA = input()
num = list(map(int,input().split()))
now = [0] * 4
result = 0
for i in range(m):
    now[check(DNA[i])] += 1
if check2():
    result += 1
for i in range(n-m):
    now[check(DNA[i])] -= 1
    now[check(DNA[i+m])] += 1
    if check2():
        result += 1
print(result)