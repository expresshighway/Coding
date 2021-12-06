import sys
input = sys.stdin.readline

def dfs(v, i):
  visited[v] = True
  for x in arr[v]:
    if not (visited[x]):
      dfs(x, i)
    elif visited[x] and x == i:
      result.append(x)

N = int(input())
arr = [ [] for i in range(N+1)]
for i in range(N):
  arr[i+1].append(int(input())) 

result = []
for i in range(1, N+1):
  visited = [False] * (N+1)
  dfs(i, i)
length = len(result)
print(length)
for i in range(length):
  print(result[i])