# import sys
# input = sys.stdin.readline

# n =  int(input())
# xy = [list(map(int, input().split())) for _ in range(n)]
# xy.sort(key=lambda x: x[0])
# start = xy[0][0]
# end = 0
# answer = 0

# for i in range(n-1):
#   if (xy[i][1] >= xy[i+1][0]):
#     end = xy[i+1][1]
#   else:
#     answer = (end - start) + answer
#     start = xy[i][0]
#     end = xy[i][1]

# print(answer)

import sys
input = sys.stdin.readline
 
N = int(input())
lines = []
 
for _ in range(N):
    s, n = map(int, input().split())
    lines.append((s, n))
 
lines.sort()
ans = 0
bS = bE = 0
 
for s, e in lines:
    if not ans:
        ans = abs(e - s)
        bS = s
        bE = e
        continue
 
    if bS <= s and bE >= e:
        continue
    
    ans += abs(e - s)
 
    if bE > s:
        ans -= abs(bE - s)
    
    bS = s
    bE = e
 
print(ans)