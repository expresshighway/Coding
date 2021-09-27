import sys
input = sys.stdin.readline

n = int(input())
output = []

for i in range(n):
  A, B = map(int, input().split())
  output.append(A+B)

for j in range(n):
  print(output[j])