# 상속(Inheritance)

- 기존의 클래스로 새로운 클래스를 작성하는 것 (코드의 재사용)
- 두 클래스를 부모와 자식으로 관계를 맺어주는 것



```java
class Parent {}
class Child extends Parent{
    // ..
}
```



- 자손은 조상의 모든 멤버를 상속받는다.(생성자,  초기화블럭 제외)

- 자손의 멤버 개수는 조상보다 적을 수 없다(같거나 많다.)
- 자손의 변경은 조상에 영향을 미치지 않는다.

```java
class Child extends Parent {
    void play() {
        System.out.println("놀자~");
    }
}
```



## 포함 관계

- 클래스의 멤버로 참조변수를 선언하는 것
- 작은 단위의 클래스를 만들고, 이 들을 조합해서 클래스를 만든다

```java
class Circle {
    Point c = new Point(); // 원점 -> Circle이 Point를 포함
    int r; // 반지름
}

class Car {
    Engine e = new Engine(); // 엔진
    Door...
}
```

 

- 상속관계 : '~은 ~이다(is-a)'

- 포함관계 '~은 ~을 가지고 있다(has - a)'



### 단일 상속(Single Inheritance)

- Java는 단일 상속만을 허용 -> 인터페이스 사

```java
class TvDVD extends Tv, DVD{ // 에러 조상은 하나만 허용
    // ..
}
```

- 비중이 높은 클래스 하나만 상속관계로, 나머지는 포함관계로 한다.



### Object클래스 - 모든 클래스의 조상

- 부모가 없는 클래스는 자동적으로 Object를 상속받게 된다.

- 모든 클래스는 Object클래스에 정의된 11개의 메서드를 상속받는다.

  - toString(), equals(Object obj), hashCode(),...

  



### 오버라이딩의 조건

1. 선언부가 조상 클래스의 메서드와 일치해야 한다.
2. 접근 제어자를 조상 클래스의 메서드보다 좁은 범위로 변경할 수 없다.
3. 예외는 조상 클래스의 메서드보다 많이 선언할 수 없다.



### 오버로딩 vs. 오버라이딩

- 오버로딩: 기존에 없는 새로운 메서드를 정의하는 것(new) 
  - 이름이 같은 새로운 메서드
- 오버라이딩: 상속받은 메서드의 내용을 변경하는 것(change, modify)

 