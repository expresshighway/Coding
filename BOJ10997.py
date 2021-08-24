n = int(input())

width = 4*n - 3
height = 4*n - 1

star = [[' ' for _ in range(width)] for _ in range(height)]

def fill (n, x, y):
  if n == 1:
    star[y][x] = "*"
    star[y+1][x] = "*"
    star[y+2][x] = "*"

  else:
    for i in range(4*n - 4):
      star[y][x] = "*"
      x-=1
    for i in range(4*n - 2):
      star[y][x] = "*"
      y += 1
    for i in range(4*n -4):
      star[y][x] = "*"
      x += 1
    for i in range(4*n - 4):
      star[y][x] = "*"
      y -= 1

    star[y][x] = "*"
    star[y][x - 1] = "*"
    fill(n-1, x-2, y)

if n == 1:
  print("*")

else:
  fill(n, width-1, 0)
  for k in star:
    print(''.join(k).rstrip())
