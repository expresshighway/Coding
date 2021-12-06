N, K = map(int, input().split())
A = []
for i in range(N):
  A.append(int(input()))
A.reverse()

count = 0
for i in A:
  count += K // i
  K %= i
print(count)