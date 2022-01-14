import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for i in range(n):
  stairs.append(int(input()))
dp = [0] * n

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]

for i in range(2, n):
  dp[i] = max(dp[i-2] + stairs[i], dp[i-3]+stairs[i]+stairs[i-1])

print(dp[n-1])
