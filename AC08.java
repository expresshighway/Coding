package Baekjoon;
import java.io.*;
import java.util.*;

public class AC08 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int max = N*(N-1)/2;
		double arr[]= new double[N];
		for (int i=0;i<N;i++) {
			String[] s = br.readLine().split(" ");
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			arr[i] = (double)b/(double)a;
		}
		
		double tmp = arr[0];
		int sum = 0;
		int sub = 0;
		for (int j=0; j<arr.length; j++) {
			if(tmp == arr[j]) {
				sum=sum+1;
			}
			else {
				if(sum == 1) {
					tmp = arr[j];
					sum = 0;
				}
				else {
					sub = sub+sum*(sum-1)/2;	
					tmp = arr[j];
					sum = 1;
				}
			}
		}
		System.out.println(sub);
		int answer = (N*(N-1))/2 - sub;
		System.out.println(answer);
	}

}
