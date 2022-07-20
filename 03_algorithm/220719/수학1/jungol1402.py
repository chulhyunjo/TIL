n, k = map(int, input().split())
aliquot = []
for i in range(1,n+1):
    if n % i == 0:
        aliquot.append(i)
if len(aliquot) < k:
    print(0)
else:
    print(aliquot[k-1])