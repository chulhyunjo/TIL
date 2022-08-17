# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

def fibo(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

memo = [0] * 5001
memo[0] = 0
memo[1] = 1
for i in range(5000):
    print(i, fibo(i))