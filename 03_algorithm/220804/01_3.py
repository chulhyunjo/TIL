n, m = map(int,input().split())
max_number = 0
for i in range(n):
    array = list(map(int,input().split()))
    min_number = min(array)
    max_number = max(max_number, min_number)

print(max_number)