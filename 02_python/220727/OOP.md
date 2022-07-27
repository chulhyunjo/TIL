## 객체지향의 핵심 4가지

- 추상화
- 상속
- 다형성
- 캡슐화



### 상속

- 두 클래스 사이 부모 - 자식 관계를 정립하는 것
- 클래스는 상속이 가능함
  - 모든 파이썬 클래스는 Object를 상속 받음

`class ChildClass(ParentClass):`

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- 부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아진다.



##### isinstance(object, classinfo)

- classinfo의 instance거나 subclass*인 경우 True

##### issubclass(class, classinfo))

- class가 classinfo의 subclass면 True

##### super()

- 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
 
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super.__init__(name, age, nuber, email)
        self.student_id = student_id
```





#### 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨



#### mro 메서드(method resolution order)

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 기존의 인스턴스 > 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 > 자식 클래스 > 부모클래스로 확장



### 다형성

- 여러 모양을 뜻하는 그리스어
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 즉, 서로 다른 클래스에 속해 있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음



#### 메서드 오버라이딩(덮어쓰기)

- 상속받은 메서드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용



### 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단
  - 예시 : 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로 존재하지 않음



#### getter 메서드와  setter 메서드

- 변수에 접근할 수 있는 메서드를 별도로 생성
  - getter 메서드 : 변수의 값을 읽는 메서드
    - @property데코레이터 사용
  - setter 메서드: 변수의 값을 설정하는 성격의 메서드
    - @변수.setter 사용

getter > 조회, setter> 변경



`raise` 함수 오류를 발생시키는 함수

