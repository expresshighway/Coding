//https://www.acmicpc.net/problem/11726
package Baekjoon;
import java.util.*;
public class BOJ11726 {
	static int [] arr;
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		arr = new int[n+1];
		
		arr[0] = 1;
		arr[1] = 1;
		
		for(int i=2; i<=n; i++) {
			arr[i] = (arr[i-1]+arr[i-2]) % 10007;
		}
		System.out.println(arr[n]);
		
		//System.out.println(top_down(n));
		sc.close();
	}
	
	static public int top_down(int n) {
		if(arr[n] > 0)
			return arr[n];
		else {
			arr[n] = (top_down(n-1)+top_down(n-2)) % 10007;
			return arr[n];
		}
	}
}
