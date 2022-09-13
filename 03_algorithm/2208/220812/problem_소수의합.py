def isPrime(n):
    if n == 2: # 2는 소수
        return 1
    elif n % 2 == 0: # 2의 배수는 소수 x
        return 0
    else:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return 0
            i += 1
        return 1


for tc in range(1, int(input())+1):
    a, b = map(int,input().split())
    cnt = 0
    for i in range(a+1, b):
        cnt += i * isPrime(i)
    print(f'#{tc} {cnt}')