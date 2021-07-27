import sys
import heapq

input = sys.stdin.readline
table = []
room = []

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
table.sort(key=lambda x: x[0])

room = []
heapq.heappush(room, table[0][1])

for i in range(1, N):
  if room[0] > table[i][0]:
    heapq.heappush(room, table[i][1])
  else:
    heapq.heappop(room)
    heapq.heappush(room, table[i][1])

print(len(room))