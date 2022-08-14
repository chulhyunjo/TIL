def primeList(a,b):
    erasto = [True] * (b+1)
    erasto[0] = erasto[1] = False

    for i in range(2, int(b**0.5) + 1):
        if erasto[i] == True:
            for j in range(i+i, b+1, i):
                erasto[j] = False

    return [k for k in range(a,b+1) if erasto[k] == True]


x, y = map(int,input().split())
# if x >= 10000000:
#     x = 10000000
# if y >= 10000000:
#     y = 10000000
prime = primeList(x, y)
for i in prime:
    if str(i) == str(i)[::-1]:
        print(i)
else:
    print(-1)