import java.util.Scanner;
public class Main2 {
	static int[] num,op;
	static int maxV, minV, N;
	public static void ogo(int p, int mi, int mul, int div,int cnt,int res) {
		if(cnt == N-1) {
			if(res>maxV)
				maxV = res;
			if(res<minV)
				minV = res;
		}
		else {
			if(p>0)
				ogo(p-1,mi,mul,div,cnt+1,res+num[cnt+1]);
			if(mi>0)
				ogo(p,mi-1,mul,div,cnt+1,res-num[cnt+1]);
			if(mul>0)
				ogo(p,mi,mul-1,div,cnt+1,res*num[cnt+1]);
			if(div>0)
				if(res<0)
					ogo(p,mi,mul,div-1,cnt+1,-(-res/num[cnt+1]));
				else
					ogo(p,mi,mul,div-1,cnt+1,res/num[cnt+1]);
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		N = n;
		num = new int[n];
		op = new int[4];
		maxV = -1000000000;
		minV = 1000000000;
		for(int i=0; i<n; i++) {
			num[i] = sc.nextInt();
		}
		for(int j=0; j<4; j++) {
			op[j] = sc.nextInt();
		}
		ogo(op[0],op[1],op[2],op[3],0,num[0]);
		System.out.println(maxV);
		System.out.println(minV);
	}
}
