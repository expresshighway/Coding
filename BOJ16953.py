from collections import deque
a, b = map(int, input().split())
que = deque([(a, 1)])
num = -1
while que:
  i, count = que.popleft()
  if i == b:
    num = count
    break
  if i*2 <= b:
    que.append((i*2, count+1))
  if (int(str(i)+'1') <= b):
    que.append((int(str(i)+'1'), count+1))

print(num)