array = set()
for _ in range(int(input())):
    array.add(input())

array = list(array)
array = sorted(sorted(array), key = len)
for i in array:
    print(i)