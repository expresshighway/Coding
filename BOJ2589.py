import sys
from collections import deque
input = sys.stdin.readline
count = 0
h, w = map(int, input().split())
visited = [[False]*w for _ in range(h)]
dia = [input().split() for i in range(int(h))]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs(i, j):
  queue = deque()
  queue.append((i, j, 0))
  visited[i][j] = True
  num = 0
  while queue:
    x, y, distance = queue.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if nx < 0 or nx >= h or ny < 0 or ny >= w:
          continue
      if visited[nx][ny] is False and dia[nx][ny] == 'L':
          queue.append((nx, ny, distance+1))
          visited[nx][ny] = True
          num = max(num, distance+1)
  return num

for i in range(h):
  for j in range(w):
    if dia[i][j] != "W":
      count = max(count, bfs(i, j))

print(count)

