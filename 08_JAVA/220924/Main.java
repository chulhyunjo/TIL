import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] sugar = new int[n+1];
		for(int i=1; i<=n; i++) {
			if(i%5 == 0||(i-3)%5==0 & (i-3)>0)
				sugar[i] = sugar[i-5]+1;
			else if (i%3==0||(i-5)%3==0 & (i-5)>0)
				sugar[i] = sugar[i-3]+1;
		}
		
		int result;
		if(sugar[n]==0)
			result=-1;
		else
			result=sugar[n];
		System.out.println(result);
	}
}
