import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end, bridge, n):
  queue = deque()
  queue.append(start-1)
  visited = [-1] * n
  visited[start-1] = 0
  
  while queue:
    node = queue.popleft()
    
    for i in range(node, n, bridge[node]):
      if visited[i] == -1:
        visited[i] = visited[node] + 1
        queue.append(i)
        if i == end-1:
          return visited[i]
    
    for i in range(node, -1, -bridge[node]):
      if visited[i] == -1:
        visited[i] = visited[node] + 1
        queue.append(i)
        if i == end-1:
          return visited[i]
  return -1

n = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())

print(bfs(start, end, bridge, n))

