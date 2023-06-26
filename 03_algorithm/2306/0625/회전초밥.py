import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

left = 0
right = 0
max_cnt = 0

eat = [0] * (d+1)
nums = 0
while right < N:
    eat[sushi[right]] += 1
    if eat[sushi[right]] == 1:
        nums += 1
    if sushi[right] == c and eat[c] == 1:
        right += 1
        nums += 1
    if right >= k - 1:
        max_cnt = max(max_cnt, nums)
        while right - left != k and eat[c] == 0:
            eat[sushi[left]] -= 1
            if eat[sushi[left]] == 0:
                nums -= 1
            left += 1
        if right - left != k:
            eat[sushi[left]] -= 1
            if eat[sushi[left]] == 0:
                nums -= 1
            left += 1
    right += 1

print(max_cnt)