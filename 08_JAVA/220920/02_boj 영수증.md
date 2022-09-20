## boj 영수증

```java
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long total = sc.nextInt();
		int n = sc.nextInt();
		int result = 0;
		for (int i=0; i<n; i++) {
			int mon = sc.nextInt();
			int num = sc.nextInt();
			result += (mon*num);
		}
		if (result == total) {
			System.out.print("Yes");
		}
		else {
			System.out.print("No");
		}
	}
}
```

