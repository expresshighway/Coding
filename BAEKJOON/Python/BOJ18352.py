import sys
from collections import deque

input = sys.stdin.readline
result = []

def bfs(a):
  queue = deque()
  queue.append(a)
  visited[a] = 1
  distance[a] = 0
  
  while queue:
    a = queue.popleft()
    for k in city[a]:
      if visited[k] == 0:
        visited[k] = 1
        queue.append(k)
        distance[k] = distance[a] + 1
        if distance[k] == K:
          result.append(k)
  if len(result) == 0:
    print(-1)
  else:
    result.sort()
    for i in result:
      print(i, end='\n')


N, M, K, X = map(int, input().split())
city = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
distance = [0] * (N+1)

for i in range(M):
  x, y = map(int, input().split())
  city[x].append(y)
  
bfs(X)