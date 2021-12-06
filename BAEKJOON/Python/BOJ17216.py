import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
prefixValue = A[0]
sum = 0

for i in range(1, N):
  if (A[i] == A[-1]) and (prefixValue > A[i]):
      sum += A[i]
      sum += prefixValue
  elif prefixValue > A[i]:
    sum += prefixValue
  prefixValue = A[i]

print(sum)

