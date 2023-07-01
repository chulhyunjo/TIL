## String클래스

- String클래스 = 데이터(char[]) + 메서드(문자열 관련)
- 내용을 변경할 수 없는 불변 클래스
- 덧셈 연산자를 이용한 문자열 결합은 성능이 떨어짐
- 문자열의 결합이나 변경이 잦다면, 내용을 변경가능한 StringBuffer를 사용



`String str = "abc"`;와 `String str = new String("abc")`의 비교

![image-20230701223110364](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20230701223110364.png)



### 빈 문자열("", empty string)

- 내용이 없는 문자열. 크기가 0인 char형 배열을 저장하는 문자열
- 크기가 0인 배열을 생성하는 것은 어느 타이나 가능

- 문자와 문자열의 초기화
  - String s = ""; 빈문자열으로 초기화
  - char c = ' '; 공백으로 초기화



## 메서드

- String(char[] value)
  - char [] c = {'H', 'e', 'l', 'l', 'o'};
  - String s = new String(c);

- String(Stringbuffer buf)

  - ```java
    StringBuffer sb = new StringBuffer("Hello");
    String s = new String(sb);
    ```

- char charAt(int index)

  - 지정된 위치에 있는 문자를 알려준다.

- int compareTo(String str)

  - 문자열과 사전순서로 비교한다.

    ```java
    int i = "aaa".compareTo("aaa"); = 0  같으면 0
    int i2 = "aaa".compareTo("bbb"); = -1 왼쪽이 작으면 -1
    int i3 = "bbb".compareTo("aaa"); = 1  오른쪽이 작으면 1
    ```

  - 정렬할때 사용

- String concat(String str)

  - 문자열 뒤에 덧붙인다.

- boolean contains(CharSequence s)

  - ```java
    String s = "abcedfg";
    boolean b = s.contains("bc"); -> true
    ```

- boolean endsWith(String suffix)

  - 문자열로 끝나는지 검사

  ```java
  String s = "abcdefg";
  boolean b = s.endsWith("fg"); -> true
  ```

- boolean equals(Object obj)
  - 같은지 확인

- boolean equalsIgnoreCase(String str)
  - 대문자 구분없이 비교
- int indexOf(char c)
  - 주어진 문자가 위치한 index 없으면 -1

- int indexOf(char c, int pos)
  - 주어진 위치부터 c를 찾는다 없으면 -1
- int indexOf(String str)
  - 문자열의 시작위치를 찾는다.
- lastIndexOf(char c), (String str)
  - 지정된 문자를 뒤에서 부터 찾는다.
- int length()
  - 문자열의 길이를 알려줌
- String[] split(String regex)
  - 문자열을 분리자로 나누어 자른다
- String[] split(String regex, int limit)
  - 분리자로 나누어 문자열배열엗마아 반환
  - 문자열 전체를 지정된 수로 자른다.
- boolean startsWith(String prefix)
  - 문자열로 시작하는지 검사
- String substring(int begin, int end)
  - end가 없으면 시작위치부터 끝
- String toLowerCase()
- String toUpperCase()
- String trim
- String valueOf -> 문자열로 변환



### join()과 StringJoiner

- join()은 여러 분자열 사이에 구분자를 넣어서 결함

```java
String animals = "dog,cat,bear";
String[] arr = animals.split(","); -> ["dog","cat","bear"]
String str = String.join("-", arr);
-> "dog-cat-beak"
```



- 숫자를 문자열로 바꾸는 방법

```java
int i = 100;
String str1 = i + "";
String str2 = String.valueOf(i);
```



- 문자열을 숫자로 바꾸는 방법

```java
int i = Integer.parseInt("100");
int i2 = Integer.valueOf("100");
```

parseXX -> valueOf으로 통일