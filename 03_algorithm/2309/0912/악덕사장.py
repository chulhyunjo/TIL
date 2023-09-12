N = int(input())
A = list(map(int,input().split()))
A.sort()

K = int(1e9)
for i in range(1, N+1):
    k = A[i-1] // i
    K = min(k, K)

print(K)