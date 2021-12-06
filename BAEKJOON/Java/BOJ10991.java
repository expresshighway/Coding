package Baekjoon;

import java.util.Scanner;
public class BOJ10991 {
	public static void main(String[] args) {
			
			Scanner input = new Scanner(System.in);
			int star;
			
			star = input.nextInt();
			for (int i=1; i<=star; i++) {
				for (int k=star-i; k>0; k--)
					System.out.print(' ');
				for (int j=0; j<i; j++) {
					System.out.print('*');
					System.out.print(' ');
				}			
				System.out.println();
			}
		input.close();
		}
}
