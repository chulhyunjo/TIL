lst = [0,0,0,1,3,2,4,5,2,2,1,3,4,5,6,7,3,6,7,7]
cnt = [0] * 8
new_arr = [0] * len(lst)
for i in range(len(lst)):
    cnt[lst[i]] += 1

for i in range(1,len(cnt)):
    cnt[i] += cnt[i-1]

for i in range(len(lst)):
    new_arr[cnt[lst[i]]-1] = lst[i]
    cnt[lst[i]] -= 1

print(new_arr)