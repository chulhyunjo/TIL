## Counter

> 자동으로 입력받은 자료로부터 키와 값 형태로 각 요소의 개수를 계산

- 각 요소는 키가 되고, 요소의 개수가 값이 된다.

- 가장 많은 개수를 가진 요소를 순새대로 뽑을 수도 있다.
- 연산자를 통해 모듈의 객체들끼리 연산이 가능



```python
from collections import Counter
# 라이브러리 import

array = [1,2,3,4,1,2,3,1,2,3,4,5,1,2,3]
# 리스트를 선언

d = Counter(array)
# Counter({1: 4, 2: 4, 3: 4, 4: 2, 5: 1})

print(d[1]) # 4 
print(d[2]) # 4

```



### elements()

> Counter안의 요소들을 출력이 가능하다.

```python
d = Counter({'apple': 2, 'banana': 0, 'cherry': 3})
for elem in d.elements():
    print(elem)
# apple
# apple
# cherry
# cherry
# cherry
```



### most_common([n])

> 가장 많은 개수를 가진 값들을 출력할 수 있다.

```python
d = Counter('abcdeaceab')
print(d.most_common())
# [('a', 3), ('b', 2), ('c', 2), ('e', 2), ('d', 1)]

print(d.most_common(2))
# [('a', 3), ('b', 2)]
```

```python
from collections import Counter
for tc in range(int(input())):
    t = int(input())
    array = list(map(int, input().split()))

    most = Counter(array).most_common(1)

    print(f'#{t} {most[0][0]}')
```

### subtract

> 빼기

```python
d1 = Counter(red=1, green=3, blue=5, black=0)
d2 = Counter(red=3, green=1, black=2)
d1.subtract(d2)
print(d1)
# Counter({'blue': 5, 'green': 2, 'red': -2, 'black': -2})
```



### update()

> 더하기

```python
d1 = Counter(red=1, green=3, blue=5, black=0)
d2 = Counter(red=3, green=1, black=2)
d1.update(d2)
print(d1)
# Counter({'blue': 5, 'red': 4, 'green': 4, 'black': 2})
```



