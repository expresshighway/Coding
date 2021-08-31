import sys
from math import gcd
input = sys.stdin.readline
n, m, t = map(int, input().split())
m = max(n, m)
n = min(n, m)

def lcm(x, y):
  return x * y // gcd(x, y)

num = t // lcm(n, m)
rest = t % lcm(n, m)

answer1 = num // n

print(answer1)