import java.util.Scanner;
public class ArrayPractice {
	public static void main(String[] args) {
		int intArray [] = new int[5];
		int sum=0;
		
		Scanner sc = new Scanner(System.in);
		System.out.print(intArray.length + "개의 정수를 입력하세요");
		for(int i=0; i<intArray.length; i++) {
			intArray[i] = sc.nextInt();
		}
		for (int k : intArray)
			sum += k;
		
		System.out.println("평균은  " + (double)sum/intArray.length + "입니다.");
	}
}
