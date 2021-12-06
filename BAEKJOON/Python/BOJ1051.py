n, m = map(int, input().split())
num = []

for i in range(n):
  num.append(list(input()))

min_num = min(n, m)
answer = 0
for i in range(n):
  for j in range(m):
    for k in range(min_num):
      if ((i+k) < n) and ((j+k) < m) and (num[i][j] == num[i][j+k] == num[i+k][j] == num[i+k][j+k]):
        answer = max(answer, (k+1)**2)

print(answer)