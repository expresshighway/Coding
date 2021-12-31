import sys
from collections import deque

input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append([0, 0])
  visited[0][0] = True
  
  while queue:
    a, b = queue.popleft()
    check = map[a][b]
    
    if check == -1:
      print("HaruHaru")
      return
    
    for dx, dy in (1, 0), (0, 1):
      x = a + dx * check
      y = b + dy * check
      
      if 0 <= x < n and 0 <= y < n and visited[x][y] == False:
        queue.append([x, y])
        visited[x][y] = True
  print("Hing")    
  
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n  for _ in range(n)]
bfs()