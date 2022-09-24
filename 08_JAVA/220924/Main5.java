import java.util.Arrays;
import java.util.Scanner;
public class Main5 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for(int i=0; i<n; i++) {
			int num = sc.nextInt();
			arr[i] = num;
		}
		Arrays.sort(arr);
		for(int j=0; j<n; j++) {
			System.out.println(arr[j]);
		}
	}
}
