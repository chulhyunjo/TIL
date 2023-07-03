# StringBuffer 클래스

- String처럼 문자형 배열(char[])을 내부적으로 가지고 있다.

```java
public final class StringBuffer implements java.io.Serializable{
    private char[] value;
}
```

- String과 달리 내용을 변경할 수 있다.

```java
String Buffer sb = new StringBuffer("abc");
sb.append("123");
// delete(), insert()
```



- 배열은 길이 변경불가. 공간이 부족하면 새로운 배열을 생성해야한다.

- StringBuffer는 저장할 문자열의 길이를 고려해서 적절한 크기로 생성해야 한다.

- StringBuffer는 equals()가 오버라이딩 되어 있지 않다.(주소 비교)
- String으로 변환후 equals()로 비교해야함

```java
String s = sb.toString();
String s2 = sb.toString();
s.equals(s2) // true
```



### 메서드

```java
StringBuffer sb = new StringBuffer(16); // 길이를 설정할 수 있다.
// 16문자를 담을 수 있는 버퍼

sb.append("ABC").append(123);
// 어떤 타입을 넣든 문자열로 변경 후 삽입

int bufferSize = sb.capacity(); // 버퍼의 크기
int stringSize = sb.length(); 	// 담긴 문자열의 길이
char c = sb.charAt(2);			// 2가 담긴 위치 반환
StringBuffer sb2 = sb.delete(3, 6);	// 3~5 지우기
sb.deleteCharAt(3);				// 3 위치 문자 제거
sb.inser(4, '.');				// 정해진 위치에 삽입
sb.replace(3, 6, "AB");			// 3~5를 "AB"로 변경
sb.reverse();					// 뒤집기
sb.setCharAt(5, 'o');			// 지정 위치의 문자를 바꾸기
sb.setLength(5);				// 지정된 길이로 문자열의 공간의 길이를 변경, 비어있으면 " "공백
sb.toString();					// 문자열로 반환
String str = sb.subString(3);	// 지정 위치부터 (end)까지 잘라내기
```

