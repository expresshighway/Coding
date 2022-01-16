import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

count = 0

for i in range(n-1, -1, -1):
  if i + time[i][0] > n:
    dp[i] = dp[i+1]
  else:
    dp[i] = max(time[i][1] + dp[i + time[i][0]], dp[i+1])

print(dp[0])