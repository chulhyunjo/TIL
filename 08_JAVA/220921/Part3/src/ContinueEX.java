import java.util.Scanner;
public class ContinueEX {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("정수 5개를 입력하시오:");
		int sum = 0;
		for(int i=0; i<5; i++) {
			int n = sc.nextInt();
			if(n <= 0) {
				continue;
			}
			else {
				sum += 1;
			}
		}
		System.out.print(sum);
	}
}
