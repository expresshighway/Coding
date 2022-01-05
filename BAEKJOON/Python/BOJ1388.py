import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
floor = []

for i in range(N):
  floor.append(list(input()))
count = 0

for i in range(N):
  pre = '/'
  for j in range(M):
    if floor[i][j] == '-':
      if floor[i][j] != pre:
        count += 1
      pre = floor[i][j]
  for j in range(M):
    if floor[i][j] == '|':
      if floor[i][j] != pre:
        count += 1
      pre = floor[i][j]
  
print(count)