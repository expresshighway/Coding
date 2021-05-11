import sys
candy = 0
M, N = map(int, sys.stdin.readline().strip().split())
friend = sorted([int(sys.stdin.readline()) for _ in range(N)])

rest = sum(friend) - M

answer = 0
for i in range(N):
  num = min(friend[i], rest // (N-i))
  answer += num * num
  rest -= num

print(answer % (pow(2,64)))