import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
  queue = deque()
  queue.append(x)
  
  while queue:
    v = queue.popleft()
    for i in range(1, miro[v]+1):
      if (v + i) >= N or visited[v + i] != 0:
        continue
      visited[v + i] = visited[v] + 1
      queue.append(v+i)

N = int(input())

miro = list(map(int, input().split()))
visited = [0] * N

if N == 1:
  print(0)
else:
  bfs(0)
  print(visited[-1] if visited[-1] != 0 else -1)


  