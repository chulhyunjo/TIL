num1 = int(input())
num2 = input().strip()
result = []
for i in num2[::-1]:
    i = int(i)
    result.append(i*num1)
cnt = 0
summ = 0
for j in result:
    print(j)
    summ += j * 10**cnt
    cnt += 1

print(summ)

