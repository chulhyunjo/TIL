n = int(input())

for i in range(n):
    lst = list(map(int, str(i)))
    result = i + sum(lst)
    if result == n:
        print(i)
        break

else:
    print(0)