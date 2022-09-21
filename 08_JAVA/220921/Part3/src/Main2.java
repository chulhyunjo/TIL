import java.util.Scanner;
public class Main2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt();
		int n2 = sc.nextInt();
		
		int first = n1 * (n2%10);
		int second = n1 * (n2%100/10);
		int third = n1 * (n2/100);
		int result = first + 10*second + 100* third;
		System.out.printf("%d\n%d\n%d\n%d\n",first,second,third,result);
	}
}
