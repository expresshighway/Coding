import sys
from collections import deque

input = sys.stdin.readline

def bfs(node, number):
  queue = deque()
  queue.append((node, number))
  while queue:
    node, number = queue.popleft()
    for n in [node+1, node*2, node*3]:
      if n <= N and check[n] == 0:
        if n == N:
          return check[node]+1, number+[n]
        queue.append((n, number+[n]))
        check[n] = check[node]+1

N = int(input())
if N == 1:
  print(0)
  print(1)
else:
  check = [0]*(N+1)
  count, number = bfs(1, [1])
  print(count)
  print(*number[::-1])