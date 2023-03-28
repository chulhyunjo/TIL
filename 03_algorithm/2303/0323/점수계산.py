numbers = []
for _ in range(8):
    numbers.append(int(input()))

sort_numbers = sorted(numbers, reverse=True)[:5]
print(sum(sort_numbers))
indexs = []
for num in sort_numbers:
    indexs.append(numbers.index(num)+1)
print(*sorted(indexs))
