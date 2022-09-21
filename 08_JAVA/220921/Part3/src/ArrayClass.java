
public class ArrayClass {
	public static void main(String[] args) {
		int i [] = new int[10];
		for(int sum=0,n=0; n<10; n++) {
			sum += n;
			i[n] = sum;
		}
		System.out.println(i[3]);
	}
}
