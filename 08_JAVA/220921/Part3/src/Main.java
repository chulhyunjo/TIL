import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int score[] = new int[n];
		String ox;
		int temp;
		for(int i=0; i<n; i++) {
			ox = sc.next();
			temp = 0;
			
			for(int j=0; j<ox.length(); j++) {
				if(ox.charAt(j) == 'O') {
					temp++;
				}
				else {
					temp = 0;
				}
				score[i]+=temp;
			}
			System.out.println(score[i]);
		}
		sc.close();
	}
}
