# import sys

# input = sys.stdin.readline
# N = input()
# arr = []

# for i in N:
#   arr.append(i)

# for i in sorted(arr, reverse=True):
#   print(i, end='')


print(''.join(reversed(sorted(input()))))