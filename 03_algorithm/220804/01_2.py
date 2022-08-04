n, m, k = map(int,input().split())
numbers = sorted(list(map(int,input().split())), reverse=True)
result = 0

# cnt = 0
# for _ in range(m):
#     if cnt == k:
#         cnt = 0
#         result += numbers[1]
#     else:
#         result += numbers[0]
#         cnt += 1
#
# print(result)
count = int(m/(k+1)) * k
print(count)
count += m % (k+1)
print(count)
result += count * numbers[0]
result += (m-count) * numbers[1]
print(result)