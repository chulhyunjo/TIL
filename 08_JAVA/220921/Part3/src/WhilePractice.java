import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class WhilePractice {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int maxV=-1000001, minV=1000001;
		while(st.hasMoreTokens()) {
			int m = Integer.parseInt(st.nextToken());
			if(maxV < m) {
				maxV = m;
			}
			if(minV>m) {
				minV = m;
			}
		}
		System.out.printf("%d %d", minV, maxV);
		
	}
}
