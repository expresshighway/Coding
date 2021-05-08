package Baekjoon;

import java.util.Scanner;
import java.lang.Math;

public class BOJ1699 {
    public static int dp[];

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        dp = new int[num+1];

        for (int i = 1; i <= num; i++){
            dp[i] = i;
            for (int j = 1; j*j <= i; j++){
                if (dp[i] > dp[i-j*j]+1){
                    dp[i] = dp[i-j*j]+1;
                }
            }
        }
        System.out.println(dp[num]);
    }
}