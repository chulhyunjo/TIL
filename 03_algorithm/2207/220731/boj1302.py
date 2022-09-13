array = []
n = int(input())
for _ in range(n):
    array.append(input())

array.sort()
max_count = 0
max_book = ''

for i in array:
    if array.count(i) > max_count:
        max_count = array.count(i)
        max_book = i

print(max_book)