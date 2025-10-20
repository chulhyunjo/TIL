n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()

start = 0
end = n-1

result = 0
while start < end:
    a, b = numbers[start], numbers[end]
    if a + b == x:
        result += 1
        start += 1

    elif a + b > x:
        end -= 1

    else:
        start += 1

print(result)