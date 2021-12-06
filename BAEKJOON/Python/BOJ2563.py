import sys
input = sys.stdin.readline

N = int(input())
array =[[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      array[i][j] = 1

answer = 0
for num in array:
  answer = answer + num.count(1);

print(answer)