import sys
candy = 0
M, N = map(int, sys.stdin.readline().strip().split())
friend = sorted([int(sys.stdin.readline()) for _ in range(N)])

rest = sum(friend) - M # 나눠주지 못하는 사탕의 개수

answer = 0
for i in range(N):
  num = min(friend[i], rest // (N-i)) # 예외적인 상황을 고려한 코드
  answer += num * num
  rest -= num

print(answer % (pow(2,64)))