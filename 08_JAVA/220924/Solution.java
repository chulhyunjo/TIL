import java.util.Scanner;
import java.util.HashMap;
public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int[] dx = new int[] {1,-1};
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int k = sc.nextInt();
			int Time = 0;
			int[][] info = new int[m][4];
			for(int i=0; i<m; i++) {
				info[i][0] = sc.nextInt();
				info[i][1] = sc.nextInt();
				info[i][2] = sc.nextInt();
				info[i][3] = sc.nextInt();
			}
			
			while(Time<m) {
				HashMap<int[], int[]> location = new HashMap<int[],int[]>();
				for(int i=0; i<info.length;i++) {
					int x = info[i][0];
					int y = info[i][1];
					int num = info[i][2];
					int d = info[i][3];
					
					if(d>=3)
						y += dx[d%2];
					else
						x += dx[d%2];
					if(x==0 | x==n-1 | y==0 | y==n-1) {
						num /= 2;
						if(d==1 | d==3)
							d+=1;
						else
							d-=1;
					location
					}
					
					
				}
			}
		}
				
		
		
	}
}
