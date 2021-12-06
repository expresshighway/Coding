package Baekjoon;

import java.util.*;

public class BOJ2193 {
    public static long [] checked;

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();
        checked = new long [N+1];

        System.out.println(dp(N));

        input.close();
    }

    public static long dp(int N){

        if(N==1) return 1;
        else if(N==2) return 1;
        else if(checked[N]!=0) return checked[N];
        else{
            return checked[N] = dp(N-1) + dp(N-2);
        }
    }
}
