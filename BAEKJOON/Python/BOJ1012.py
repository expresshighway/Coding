import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

T = int(input())

def bfs(graph, a, b):
  queue = deque()
  queue.append((a, b))
  graph[a][b] = 0
  
  while queue:
    x, y = queue.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
  return

for i in range(T):
  count = 0
  M, N, K = map(int, input().split())
  graph = [[0] * N for _ in range(M)]
  print(graph)
  for j in range(K):
    x, y = map(int, input().split())
    graph[x][y] = 1
  
  for a in range(M):
    for b in range(N):
      if graph[a][b] == 1:
        bfs(graph, a, b)
        count += 1
  
  print(count)
        
  
  
