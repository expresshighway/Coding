package Baekjoon;

import java.util.Scanner;

public class BOJ1912 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = input.nextInt();
		
		int[] str = new int[N];
		int[] dp = new int[N];
		
		for(int i = 0; i < N; i++) {
			str[i] = input.nextInt();
		}
		
		dp[0] = str[0];
		int max = str[0];
		
		for (int i = 1; i < N; i++) {
			dp[i] = Math.max(dp[i - 1] + str[i], str[i]); 
			max = Math.max(max, dp[i]);
		}
		System.out.println(max);
	}

}
