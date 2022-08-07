from collections import deque
n, k = map(int,input().split())
people = deque(range(1, n + 1))
result = []
while people:
    people.rotate(-(k-1))
    result.append(people.popleft())

result = list(map(str,result))
print(f'<' + ', '.join(result) + '>')

# rotate(n) n 만큼 오른쪽으로 회전해서 rotate(2)를 할경우 [1,2,3,4,5,6] -> [6,5,1,2,3,4]
# rotate(-n) n 만큼 왼쪽으로 회전 [1,2,3,4,5,6] -> [3,4,5,6,1,2]