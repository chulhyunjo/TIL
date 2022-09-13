n = int(input())
arr = list(map(int,input().split()))

sorted_arr = sorted(list(set(arr)))
dic = dict()
for i in range(len(sorted_arr)):
    dic[sorted_arr[i]] = i

for j in arr:
    print(dic[j] , end = ' ')