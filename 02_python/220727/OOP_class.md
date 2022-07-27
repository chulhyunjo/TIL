## 객체지향 프로그래밍(OOP)

- 객체 지향 프로그래밍이란?
- OOP 기초
  - 객체 / 인스턴스 / 클래스
  - 클래스
  - 메서드



### 객체 지향 프로그래밍

- 컴퓨터 프로그래밍의 패러다임(방법론) 중 하나이다
- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러개의 독립된 단위
- 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
  - 예시
    - 콘서트
      - 가수 객체
      - 감독 객체
      - 관객 객체



### 장점 / 단점

- 장점
  - 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
  - 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움
- 단점
  - 설계시 많은 시간과 노력이 필요함
    - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
  - 실행 속도가 상대적으로 느림
    - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름



## 객체

- 컴퓨터 과학에서 객체 또는 오브젝트는 **클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것**
- **속성**과 **행동**으로 구성된 모든 것
- 클래스로 만든 객체를 인스턴스 라고도 함ㅁ
  - 객체와 인스턴스의 차이점?
    - 이찬혁은 객체이다(O)
    - 이찬혁은 인스턴스다(X)
    - 이찬혁은 가수의 인스턴스다(O)



#### 특징

- 타입 : 어떤 연산자와 조작이 가능한가?
- 속성 : 어떤 상태를 갖는가?
- 조작법 : 어떤 행위를 할 수 있는가?



### 기본 문법

- 클래스 정의 `class Myclass:` 대문자로 시작
- 인스턴스 생성 `my_instance = Myclass()`
- 메서드 호출 `my_instance.my_method()`
- 속성 `my_instance.my_attribute`



### 클래스와 인스턴스

- 클래스 : 설계도
- 인스턴스 : 하나하나의 실체

```python
class Person:
    pass

print(type(Person)) # <class 'type'>

person1 = Person()

print(isinstance(person1, Person)) # True
print(type(person1)) #  <class '__main__.Person'>
```



### 객체 비교하기

- ==
  - 동등한(equal)
  - 변수가 참조하는 객체가 동등한 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한(identical)
  - 두 변수가 동일한 객체를 가리키는 경우 True

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True False

a = [1, 2, 3]
b = a
print(a == b, a is b) # True True
```



### 속성

- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 클래스 변수 / 인스턴스 변수가 존재

```python
class Person:
    blood_color = 'red' # 클래스 변수
    population = 100 # 클래스 변수
    
    def __init__(self, name):
        self.name = name # 인스턴스 변수
person1 = Person("지민")
print(person1.name) # 지민
```



### 인스턴스 변수란?

- 인스턴스가 개인적으로 가지고 있는 속성(arrtibute)
- 각 인스턴스들의 고유한 변수
- 생성자 메서드(\__init__)에서 self.\<name>으로 정의
- 인스턴스가 생성된 이후 instance.name으로 접근 및 할당

```python
class Person:
    def __init__(self, name):
        self.name = name
john = Person('john')
print(john.name) # john
john.name = 'John Kim'
print(john.name) # John Kim
```



### 클래스 변수

- 클래스 선언 내부에서 정의
- classname.name으로 접근 및 할당

```python
class Circle():
    pi = 3.14
    
    def __init_(self, r):
        self.r = r # 인스턴스 변수
c1 = Circle(5)
c2 = Circle(10)
```



#### 활용(사용자 수 계산하기)

- 사용자가 몇명인지 확인하고 싶다면?
  - 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정하면 됨

```python
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
person1 = Person('아이유')
person2 = Person('이찬혁')

print(Person.count)
```



### 클래스 변수와 인스턴스 변수

- 클래스 변수를 변경할 때는 항상 **클래스.클래스변수** 형식으로 변경

```python
class Circle():
    pi = 3.14
    
    def __init__(self, r):
        self.r = r #인스턴스 변수
c1 = Circle(5)
c2 = Circle(10)

Circle.pi = 5 # 클래스변수 변경
c1.pi = 5 # 인스턴스 변수 변경
```



## OOP 메서드

> 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

```python
class Person:
    def talk(self):
        print('안녕')
    def eat(self, food):
        print(f'{food}를 냠냠')
```

메서드 > 클래스 안에있는 함수다.



### 메서드의 종류

- 인스턴스 메서드 > 인스턴스 처리 (개별 행동)
- 클래스 메서드 > 클래스 처리
- 정적 메서드 > 



#### 인스턴스 메서드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드

- 클래스 내부에 정의되는 메서드의 기본

- 호출 시, 첫번째 인자로 인스턴스 자기 자신(self)이 전달됨

  ```python
  class MyClass:
      
      def instance_method(self, arg1, ...):
          
  my_instance = MyClass()
  my_instance.instance_method(...)
  ```



##### self

- 인스턴스 자기 자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 쉽게



##### 생성자 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기 값을 설정
  	- 인스턴스 생성
  	- \__init__메서드 자동 호출



##### 매직 메서드

- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로 스페셜 메서드 혹은 매직 메서드라고 불림
- 특정 상황에서 자동으로 불리는 메서드



- 예시
- 객체의 특수 조작 행위를 지정(함수, 연산자 등)
- \__str__ : 해당 객체의 출력 형태를 지정
  - 프린트 함수를 호출할 때, 자동으로 호출
  - 어떤 인스턴스를 출력하면 \__str__의 return 값이 출력
- \__gt__ :  부등호 연산자(>, greater than)



#### 클래스 메서드

- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨



##### 데코레이터

- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 작동하므로 순서가 중요

```python
# 데코레이팅 함수
def add_print(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wapper

@add_print
def hello():
    print('안녕하세요')
```



##### 클래스 메서드와 인스턴스 메서드

- 클래스 메서드 > 클래스 변수 사용 cls

- 인스턴스 메서드 > 인스턴스 변수 사용

- 그렇다면 둘다 사용하고 싶다면?

  - 클래스는 인스턴스 변수 사용이 불가능
  - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능

  

##### 스태틱 메서드

- 인스턴스 변수, 클래스 변수를 전혀 다루지 안는 메서드
- 언제?
  - 속성을 다루지 않고 단지 기능만을 하는 메서드를 정의할 때, 사용

- @staticmethod



```python
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count+=1
        
    @staticmethod
    def check_rich(money): # 스태틱은 cls, self 사용x
        return money > 10000
    # 잘 사용하지는 않는다.
```



인스턴스 변수가 정의되어 있지 않으면 클래스변수(unknown)가 출력됨



