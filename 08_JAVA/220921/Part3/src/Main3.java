import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main3 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int maxV, result;
		maxV = result = 0;
		for(int i=1; i<10; i++) {
			int n = Integer.parseInt(br.readLine());
			if (n>maxV) {
				maxV = n;
				result = i;
			}
			
		}
		System.out.printf("%d\n%d", maxV, result);
	}
}
