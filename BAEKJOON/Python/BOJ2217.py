import sys

input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

answer = 0
arr.sort()
for i in range(N):
  answer = max(answer, arr[i]*(N-i))
print(answer)