import sys
from collections import deque
input = sys.stdin.readline

def bfs(a):
  queue = deque()
  queue.append(a)
  
  while(queue):
    node = queue.popleft()
    for n in graph[node]:
      if visited[n] == 0:
        visited[n] = visited[node] + 1
        queue.append(n)

n = int(input())
A, B = map(int, input().split())
m = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

bfs(A)
print(visited[B] if visited[B] > 0 else -1)