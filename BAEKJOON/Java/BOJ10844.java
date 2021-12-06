//https://www.acmicpc.net/problem/10844
package Baekjoon;
import java.util.*;

public class BOJ10844 {
	final static long mod = 1000000000;
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = input.nextInt();
		long [][] dp = new long[N+1][10];
		
		for(int i=1; i<10; i++) {
			dp[1][i] = 1;
		}
		
		for (int i=2; i<=N; i++) {
			for (int j=0; j<10; j++) {
				if (j==0) {
					dp[i][0] = dp [i-1][1] % mod;
				}
				else if (j==9) {
					dp[i][9] = dp [i-1][8] % mod;
				}
				else {
					dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod;
				}
			}
		}
		long result = 0;
		
		for (int k=0; k<10; k++) {
			result += dp[N][k];
		}
		System.out.println(result % mod);
		
		input.close();
	}

}

