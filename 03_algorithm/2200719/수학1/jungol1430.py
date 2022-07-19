a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for i in range(10):
    i = str(i)
    print(result.count(i))


