import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# dp의 의미? dp[3][7]: 6으로 끝나는 3자리 수의 계단 수의 개수

for i in range(2, n+1):
  dp[i][0] = dp[i-1][1] # 0으로 끝나는 경우
  dp[i][9] = dp[i-1][8] # 8로 끝나는 경우

  for j in range(1, 9):
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] # 1-8로 끝나는 경우

print(sum(dp[n]) % 1000000000)