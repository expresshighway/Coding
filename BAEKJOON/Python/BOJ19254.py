import sys
input = sys.stdin.readline;
N, M = map(int, input().strip().split())
num = []

for i in range(M):
  A, B, C = input().strip().split()
  num.append([int(A), int(B), C])

num.sort
