def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)


for i in range(1, 21):
    print(f(i))