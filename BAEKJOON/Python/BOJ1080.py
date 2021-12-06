import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]

def flip(x, y):
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if A[i][j] == '1':
        A[i][j] = '0'
      else:
        A[i][j] = '1'

flag = True
num = 0
for i in range(N-2):
  for j in range(M-2):
    if(A[i][j] != B[i][j]):
      num += 1
      flip(i+1, j+1)

for i in range(N):
  for j in range(M):
    if A[i][j] != B[i][j]:
      flag = False

if flag == True:
  print(num)
else:
  print(-1)