import sys
input = sys.stdin.readline

t = int(input())
test = []

for i in range(t):
  test.append(int(input()))

dp = [1, 2, 4]

for i in range(3, max(test)):
  dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in test:
  print(dp[i-1])