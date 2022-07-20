n = int(input())
array = list(map(int, input().split()))
m = int(input())
aliquot = []
multiple = []

for i in array:
    if i <= m:
        if m % i == 0:
            aliquot.append(i)
    if i >= m:
        if i % m == 0:
            multiple.append(i)

print(sum(aliquot))
print(sum(multiple))