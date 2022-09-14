def inorder(n):
    global cnt
    if n <= 2**k-1:
        inorder((2*n))
        result[n] = arr[cnt]
        cnt += 1
        inorder((2*n+1))

k = int(input())
arr = list(map(int,input().split()))
result = [0] * (2**k)
cnt = 0
inorder(1)
for i in range(k):
    print(*result[2**i:2**(i+1)])

