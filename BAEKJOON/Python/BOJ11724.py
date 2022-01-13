import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  queue = deque()
  queue.append((start))
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
for j in range(1, N+1):
  if not visited[j]:
    bfs(j)
    count += 1

print(count)