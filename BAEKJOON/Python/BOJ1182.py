# 조합문제
from itertools import combinations
N, S = map(int, input().split())
array = list(map(int, input().split()))
num = 0

for i in range (1, N+1):
    com = combinations(array, i)
    for j in com:
        # print(j, end=' ')
        if sum(j) == S:
            num = num+1 

print(num)