import java.util.Scanner;
public class ContinueEX {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("���� 5���� �Է��Ͻÿ�:");
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
