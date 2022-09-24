import java.util.Scanner;
public class Main4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int num = sc.nextInt();
		sc.close();
		int result = 0;
		for(int i=0; i<n; i++) {
			result += num % 10;
			num = num / 10;
		}
		System.out.print(result);
	}
}
