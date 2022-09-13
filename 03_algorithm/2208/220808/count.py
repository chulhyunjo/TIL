n = int(input())
arr = list(map(int,input().split()))

cnt = [0] * (n+1)
temp = arr[:]

for i in range(0,len(arr)):
    cnt[arr[i]] += 1

for i in range(1,len(cnt)):
    cnt[i] += cnt[i-1]

for i in range(len(temp)-1, -1, -1):
    cnt[arr[i]] -= 1
    temp[cnt[arr[i]]] = arr[i]

print(temp)