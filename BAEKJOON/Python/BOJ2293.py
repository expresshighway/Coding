import sys
n, k = map(int, sys.stdin.readline().split())
money = []
for i in range(n):
  money.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
# 1, 2, 5원 하나로 각각 1, 2, 5원을 만드는 경우의 수
dp[0] = 1

for j in money:
  for i in range(j, k+1):
    dp[i] += dp[i-j] # dp[i-i]에 해당 원(money)을 빼는 과정 
print(dp[k])