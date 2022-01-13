import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x, y, cx, cy):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1
  
  while(queue):
    x, y = queue.popleft()
    
    if (x == cx and y == cy):
      return visited[x][y] - 1
    
    for k in range(8):
      nx = x + dx[k]
      ny = x + dy[k]
      if (0 <= nx < l and 0 <= ny < l):
        if visited[nx][ny] == 0:
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
      

t = int(input())
for i in range(t):
  l = int(input())
  visited = [[0]*l for _ in range(l)]
  x, y = map(int, input().split())
  cx, cy = map(int, input().split())
  count = bfs(x, y, cx, cy)
  print(count)