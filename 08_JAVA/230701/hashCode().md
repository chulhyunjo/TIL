## hashCode()

- 객체의 해시코드(hash code)를 반환하는 메서드
  - 해시코드: 정수값(객체의 지문)

- Object클래스의 hashCode()는 객체의 주소를 int로 변환해서 반환

- equals()를 오버라이딩하면, hashCode()도 오버라이딩해야한다
- equals()의 결과가 true인 두 객체의 해시코드는 같아야 하기 때문이다.
- -System.identityHashCode(Object obj)는 Object클래스의 hashCode()와 동일
  - 객체마다 다른 해시코드 반환



## toString()

- 객체를 문자열으로 변환하기 위한 메서드

- toString(num, N) -> num을 N진법으로 바꾸기



### toHexString()

- 16진수로 바꾸기