from collections import deque

def find(d):
    result = 0
    if check():
        if d == n:
            if check():
                return 1
            else:
                return 0
        arr.append(numbers[d])
        result += find(d+1)
        arr.pop()
        arr.appendleft(numbers[d])
        result += find(d+1)
        arr.popleft()
        return result
    else:
        return 0

def check():
    b = -1
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            if b == 1:
                return 0
            b = 1

        else:
            if b == 0:
                return 0
            b = 0
        i += 1
    return 1

numbers = list(map(int,input().split()))
n = len(numbers)
arr = deque()
arr.append(numbers[0])

answer = find(1)
print(answer)