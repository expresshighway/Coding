import sys
input = sys.stdin.readline

N = int(input())
crane = list(map(int, input().split()))

M = int(input())
ship = list(map(int, input().split()))

sorted_crane = sorted(crane, reverse=True)
sorted_ship = sorted(ship, reverse=True)


if sorted_ship[0] > sorted_crane[0]:
      print(-1)
      sys.exit()
else:
      count = 0
      while len(sorted_ship) > 0:
            for i in range(len(sorted_crane)):
                  for j in range(len(sorted_ship)):
                        if sorted_crane[i] >= sorted_ship[j]:
                              del sorted_ship[j]
                              break
            count += 1

print(count)
