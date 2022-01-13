import sys
from collections import deque

def bfs(i):
  queue = deque()
  queue.append(i)
  visited[i] = -1
  
  while queue:
    v = queue.popleft()
    for k in tree[v]:
      if visited[k] == 0:
        queue.append(k)
        visited[k] = v
  

N = int(input())
tree = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
  x, y = map(int, input().split())
  tree[x].append(y)
  tree[y].append(x)

for j in range(1, N+1):
  if visited[j] == 0:
    bfs(j)

for n in range(2, N+1):
  print(visited[n])