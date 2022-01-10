import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
  visited[v] = 1
  queue = deque()
  queue.append(v)
  
  while queue:
    a = queue.popleft()
    print(a, end=" ")
    for i in range(1, N+1):
      if visited[i] == 0 and graph[a][i] == 1:
        queue.append(i)
        visited[i] = 1
    
def dfs(v):
  visited2[v] = 1
  print(v, end=" ")
  for i in range(1, N+1): 
    if visited2[i] == 0 and graph[v][i] == 1:
      dfs(i)
      
N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
visited2 = [0] * (N+1)

for i in range(M):
  x, y = map(int, input().split())
  graph[x][y] = graph[y][x] = 1

dfs(V)
print()
bfs(V)