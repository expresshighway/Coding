package Baekjoon;
import java.util.Scanner;

public class BOJ10992 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int star = input.nextInt();
		for (int i=1; i<=star; i++) {
			for(int k=star-i; k>0; k--) {
				System.out.print(" ");
			}
			if(i==star) {
				for(int j=1; j<=2*i-1; j++) {
					System.out.print("*");
				}
			}
			else {
				for(int j=1; j<=2*i-1; j++) {
					if(j==1 || j==2*i-1)
						System.out.print("*");
					else
						System.out.print(" ");
				}
			}
			System.out.println();
		}
		input.close();
	}
}
