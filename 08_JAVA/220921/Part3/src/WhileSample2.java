import java.util.Scanner;
public class WhileSample2 {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int count = 0;
		int sum = 0;
		System.out.println("������ �Է��ϰ� �������� -1�� �Է��Ͻÿ�");
		
		int n = sc.nextInt();
		while(n!=-1) {
			sum += n;
			count++;
			n = sc.nextInt();
		}
		if(count==0) {
			System.out.println("�Էµ� ���� �����ϴ�.");
		}
		else {
			System.out.print("������ ������" + count + "���̸�");
			System.out.println("�����" + (double)sum/count + "�Դϴ�.");
		}
	}
}
