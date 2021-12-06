package Baekjoon;
import java.util.*;
public class BOJ11727 {
	static int rec [];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		rec = new int [n+1];
		rec[0]=1;
		rec[1]=1;
		
		for (int i=2; i<=n; i++) {
			rec[i] = (rec[i-1]+2*rec[i-2]) % 10007;
		}
		System.out.println(rec[n]);
		//System.out.println(topDown(n));
		
		sc.close();
	}
	
	public static int topDown(int n) {
		if(rec[n] > 0) {
			return rec[n];
		}
		else {
			rec[n] = (topDown(n-1)+2*topDown(n-2)) % 10007;
			return rec[n];
		}
	}

}
