🔗링크 : https://www.acmicpc.net/problem/2304

# 창고 다각형

> ### 문제 설명

N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다. 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.

1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
4. 지붕의 가장자리는 땅에 닿아야 한다.
5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

![img](https://www.acmicpc.net/JudgeOnline/upload/201011/cd.png)

​																그림1 . 기둥과 지붕(굵은 선)의 예

 그림 1에서 창고 다각형의 면적은 98 ㎡이고, 이 경우가 가장 작은 창고 다각형이다.

기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.



> ### 입력

첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. (1 <= N <= 1000)

그 다음 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다. (1<= L,H <= 1000)



> ### 출력

```
7											98
2 4
11 4
15 8
4 6	
5 3
8 10
13 6
```



> ### 문제 정답

```python
import sys
input = sys.stdin.readline
n = int(input())
pos = []
height = []

for _ in range(n):
    l, h = map(int ,input().split())
    pos.append(l)
    height.append(h)

arr = [0] * (max(pos) + 1) + [0]
for i in range(n):
    arr[pos[i]] = height[i]

area = 0
maxV = max(height)
maxh = 0
for i in range(1, len(arr)-1):
    if arr[i] > maxh:
        maxh = arr[i]
    area += maxh
    if arr[i] == maxV:
        maxV = max(arr[i+1:])
        maxh = maxV

print(area)
```



> ### 문제 풀이

1. 변수 입력

```python
n = int(input()) 						# 기둥의 개수 n 입력
pos = []								# 기둥의 위치를 받을 리스트
height = []								# 위치에 따른 높이를 받을 리스트

for _ in range(n):				
    l, h = map(int ,input().split())	# l : 위치, h : 높이 띄어쓰기 기준으로 입력
    pos.append(l)						# pos 리스트에 위치 담기
    height.append(h)					# height 리스트에 높이 담기
```



2. 창고 전체를 리스트로 만들기

```python
arr = [0] * (max(pos) + 1) + [0]
for i in range(n):
    arr[pos[i]] = height[i]
```

위의 예시 입력 값을 입력하면

`arr = [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8, 0]`이 나온다.

각 위치별로 존재하는 상자의 높이를 대입



3. 창고의 넓이 구하기

```python
area = 0						# 전체 넓이를 구할 변수
maxV = max(height)				# 제일 높은 기둥의 높이
maxh = 0						# 제일 높은 기둥 제외 제일 높은 기둥 높이를 담을 변수
for i in range(1, len(arr)-1):
    if arr[i] > maxh:			# 현재 기둥의 높이가 가장 maxh 보다 클 경우
        maxh = arr[i]			# maxh = arr[i] 제일 높은 기둥의 높이를 초기화
    area += maxh				# 현재 위치에서의 넓이는 maxh만큼 증가
    if arr[i] == maxV:
        maxV = max(arr[i+1:])	# max 높이를 초기화 -> 현재 인덱스 이후 max값
        maxh = maxV
```

먼저 창고 다각형의 면적은 현재까지 가장 높이가 큰 기둥의 높이 만큼 계속 증가한다.

그래서 위와 같이 `area += maxh`를 해준다.

![img](https://www.acmicpc.net/JudgeOnline/upload/201011/cd.png)

>  가장 높이가 큰 기둥을 만났을 경우

가장 높이가 큰 기둥`(maxV)` 이후 가장 높은 기둥의 높이 만큼 area가 증가한다.

그래서 `maxV`의 값을 `max(arr[i+1:])`을 이용해서 초기화 시켜준다.

그리고 `maxh = maxV`를 통해 `area += maxh` 창고 다각형의 넓이를 꾸준히 구해준다.

