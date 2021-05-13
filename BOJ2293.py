import sys
n, k = map(int, sys.stdin.readline().split())
money = []
for i in range(n):
  money.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
# 1, 2, 5원 하나로 각각 1, 2, 5원을 만드는 경우의 수
dp[0] = 1

for i in money:
  for j in range(i, k+1):
    dp[j] += dp[j-i] # dp[j-i]에 해당 원(money)을 빼는 과정 

print(dp[k])