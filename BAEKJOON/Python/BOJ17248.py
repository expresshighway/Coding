import sys
import math
input = sys.stdin.readline;

T = int(input())
result = []
def func1 (a, b, c):
  return (-1*c + math.sqrt(c*c-4*c*(2*a-2*b)))/(2.0*c)

for i in range(T):
  X, Y, Z = map(int, input().strip().split())
  result.append(func1(X, Y, Z))

for i in range(T):
  if(result[i] - int(result[i]) > 0):
    result[i] = result[i] + 1
  print(int(result[i]))
  