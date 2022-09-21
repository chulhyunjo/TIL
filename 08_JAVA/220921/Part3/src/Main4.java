import java.util.Scanner;
public class Main4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int intArray [] = new int[10];
		int result=10 ;
		for (int i=0; i<intArray.length; i++) {
			intArray[i] = sc.nextInt()%42;
		}
		for (int i=0; i<intArray.length; i++) {
			for (int j = i+1; j<intArray.length; j++) {
				if (intArray[i] == intArray[j]) {
					result--;
					break;
				}
			}
		}
		System.out.print(result);
	}

}
