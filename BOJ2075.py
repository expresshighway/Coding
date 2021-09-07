import heapq
N = int(input())
h = []

for n in map(int, input().split()):
  heapq.heappush(h, n)
for _ in range(1, N):
  for n in map(int, input().split()):
    heapq.heappush(h, n)
    heapq.heappop(h)
print(heapq.heappop(h))