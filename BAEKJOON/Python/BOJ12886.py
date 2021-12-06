import sys
from collections import deque, defaultdict

input = sys.stdin.readline
number = list(map(int, input().split()))
visited = defaultdict(bool)
total = sum(number)

def dfs():
  queue = deque([number])
  visited[tuple(number)] = True
  while queue:
    A, B, C = queue.popleft()
    if A == B == C:
      return 1
    for x, y in ((A, B), (B, C), (A, C)):
      if x == y:
        continue
      elif x < y:
        y = y-x
        x = x*2
      else:
        x = x-y
        y = y*2
      z = total - (x+y)
      if not visited[(x, y, z)]:
        visited[(x, y, z)] = True
        queue.append([x, y, z])
  return 0

if total % 3 != 0:
  print(0)
else:
  print(dfs())
