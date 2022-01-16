import sys
input = sys.stdin.readline

t = int(input())
test = []
for i in range(t):
  test.append(int(input()))
length = max(test)

dp = [0] * length
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2

for j in range(5, length):
  dp[j] = dp[j-5] + dp[j-1]

for i in test:
  print(dp[i-1])