import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()
count = Counter(num).most_common()

result1 = round(sum(num)/N)
result2 = num[N//2]

if N > 1:
  if count[0][1] == count[1][1]:
    result3 = count[1][0]
  else:
    result3 = count[0][0]
else:
  result3 = num[0]
  
result4 = num[-1] - num[0]

# print("%.f" % result1)
print(result1)
print(result2)
print(result3)
print(result4)
