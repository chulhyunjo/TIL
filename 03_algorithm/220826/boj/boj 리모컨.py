import sys
sys.setrecursionlimit(10**9)


def dfs(l,ans):
    global result

    if len(ans) == l:
        if result and abs(int(ans)-int(target)) > result[-1]:
            return
        result.append(abs(int(ans) - int(target)))
        return

    for q in range(len(num)):
        dfs(l, ans+str(num[q]))


target = input()
n = int(input())
num = list(range(0,10))
if n != 0:
    lst = list(map(int,input().split()))
    for i in lst:
        num.remove(i)

w = ''
result = []
dfs(len(target),w)

a = min(result) + len(target)
b = min(a, abs(int(target) - 100))

print(b)