
public class CheckTime {
	public static void main(String[] args) {
		for (int i=0; i<5; i++) {
			for(int j=5-i; j>0; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
		System.out.println();
		
		int k = 0;
		while(k<5) {
			int l = 5-k;
			while (l>0) {
				System.out.print("*");
				l--;
			}
			System.out.println();
			k++;
		}
		System.out.println();
		int q=0;
		do {
			int w = 5-q;
			do {
				System.out.print("*");
				w--;
			}while(w>0);
			System.out.println();
			q++;
		}while(q<5);
		
	}
}
