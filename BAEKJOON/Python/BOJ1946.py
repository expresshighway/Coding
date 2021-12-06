import sys

n = int(input())
answer = []
count = 1
for i in range(n):
  it = int(input())
  rank = sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(it)], key = lambda x: x[0])
  max = rank[0][1]
  for j in range(1, it):
    if(rank[j][1] < max):
      count += 1
      max = rank[j][1]
  answer.append(count)
  count = 1

for i in answer:
  print(i)