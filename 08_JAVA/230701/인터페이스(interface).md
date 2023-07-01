# 인터페이스(interface)

- 추상 메서드의 집합(프로그래밍 관)
- 구현된 것이 전혀 없는 설계도. 껍데기(모든 멤버가 public)
- 추상 클래스와 인터페이스의 차이?
  - 추상 클래스는 추상 메서드를 포함한 클래스 - 일부가 추상 메서드
  - 인터페이스는 추상 메서드의 집합(iv를 가질 수 없다) - 전체가 추상 메서드

```java
interface 인터페이스이름 {
    public static final 타입 상수 이름 = 값;
    public abstract 메서드이름(매개변수 목록);
} // 모든 메서드는 public
```

```java
interface PlayingCard{
    public static final int SPADE = 4;
    final int DIAMOND = 3;
    static int HEART = 2;
    int CLOVER = 1;
    
    public abstract String getCardNumber();
    String getCardKind();		// public abstract String getCardKind();
    // 예외없이 생략이 가능(public static final, public abstract)
}
```



## 인터페이스 상속

- 인터페이스의 조상은 인터페이스만 가능(Object가 최고 조상 아님)

- 다중 상속이 가능(추상 메서드는 충돌해도 문제가 없음)
  - Object는 단일 상속만 가능(메서드의 충돌 위험)

```java
interface Fightable extends Movable, Attackable{}

interface Movable{
    void main(int x, int y);
}

interface Attackable{
    void attack(Unit u);
}
```



## 인터페이스의 구현

- 인터페이스에 정의된 추상 메서드를 완성하는 것

```java
class 클래스이름 implements 인터페이스이름{ // 상속은 extends
    // 인터페이스에 정의된 추상메서드를 모두 구현해야 한다.
}
```

- 일부만 구현하는 경우, 클래스 앞에 abstract를 붙여야 함.



Q 인터페이스란?

​	추상 메서드의 집합

Q 인터페이스의 구현이란?

​	인터페이스의 추상메서드 몸통{} 만들기(미완성 설계도 완성하기)

Q 추상 클래스와 인터페이스의 공통점

​	추상 메서드를 가지고 있다(미완성 설계도)

Q 추상 클래스와 인터페이스의 차이점은?

​	인터페이스는 iv를 가질 수 없다.



### 인터페이스를 이용한 다형성

- 인터페이스도 구현 클래스의 부모?

```java
class Fighter extends Unit implements Fightable{
    public void move(int x, int y) {}
    public void attack(Fightable f) {}
}
```



- 인터페이스를 메서드의 리턴 타입으로 지정할 수 있다.

```java
Fightable method() {
    Fighter f = new Fighter();
    return f;					// 인터페이스를 구현한 객체를 return
}
Fightable f = method();
```



### 인터페이스의 장점

- 두 대상(객체)간의 **'연결, 대화, 소통'**을 돕는 **중간 역할**을 한다
- 선언(설계)와 구현을 분리시킬 수 있게 한다.

- 개발 시간을 단축할 수 있다.

- 변경에 유리한 유연한 설계가 가능하다.
- 표준화가 가능하다.

- 관계없는 클래스들을 관계를 맺어줄 수 있다.
- 