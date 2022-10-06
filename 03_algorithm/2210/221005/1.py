import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def g(y, x, d1, d2):
    global result
    A = [0] * 5
    for i in range(N):
        for j in range(N):
            if j <= x and i < y+d1 and i+j < y+x:
                A[0] += arr[i][j]
            elif j > x and i <= y+d2 and x-y < j-i:
                A[1] += arr[i][j]
            elif j < x-d1+d2 and i >= y+d1 and x-y-d1-d1 > j-i:
                A[2] += arr[i][j]
            elif j >= x-d1+d2 and i > y+d2 and i+j > y+x+d2+d2:
                A[3] += arr[i][j]
            else:
                A[4] += arr[i][j]
    r = max(A) - min(A)

    result = r if r < result else result

    if 0 <= x-d1-1 and y+d1+d2+1 < N and (d1+1, d2) not in V:
        V.append((d1+1, d2))
        g(y, x, d1+1, d2)
    if x+d2+1 < N and y+d1+d2+1 < N and (d1, d2+1) not in V:
        V.append((d1, d2+1))
        g(y, x, d1, d2+1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = N * 20
for y in range(N-2):
    for x in range(1, N-1):
        V = [(1, 1)]
        g(y, x, 1, 1)
print(result)