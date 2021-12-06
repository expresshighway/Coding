import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sortarr = sorted(arr)

pivot=0
for i in range(N):
  if sortarr[i] < 0:
    pivot += 1

# print("pivot: %d" % pivot)

answer=0
for i in range(0, pivot, M):
  answer += abs(sortarr[i]*2)
  # print(abs(sortarr[i]*2))

for i in range(N-1, pivot-1, -M):
  answer += sortarr[i]*2
  # print(sortarr[i]*2)

answer = answer - max(abs(sortarr[0]), sortarr[N-1])
print(answer)
