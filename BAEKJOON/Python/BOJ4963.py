import sys
from collections import deque
input = sys.stdin.readline

xd = [0, 0, 1, -1, -1, -1, 1, 1]
yd = [1, -1, 0, 0, -1, 1, -1, 1]
result = []

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for k in range(8):
      nx = x + xd[k]
      ny = y + yd[k]
      
      if 0 <= nx < h and 0 <= ny < w:
        if land[nx][ny] == 1:
          land[nx][ny] = 0
          queue.append((nx, ny))

while True:
  w, h = map(int, input().split())
  if (w == 0 and h == 0):
    break
  
  land = [list(map(int, input().split())) for _ in range(h)]
  count = 0
  for i in range(h):
    for j in range(w):
      if land[i][j] == 1:
        bfs(i, j)
        count += 1
  result.append(count)
  
for i in result:
  print(i)