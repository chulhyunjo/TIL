n = int(input())
aliquot = []
for i in range(1,int(n**(0.5))+1):
    if n % i == 0:
        aliquot.append(i)
        aliquot.append(n//i)
aliquot = list(set(aliquot))
print(*sorted(aliquot))