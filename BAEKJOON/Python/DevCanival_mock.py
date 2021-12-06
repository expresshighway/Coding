# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input1 = sys.stdin.readline
N, K = map(int, input1().split())
arr = list(map(int, input().split()))
length = int(len(arr))
count = 1
while(True):
		length = length - K
		if(length <= 0):
			break
		else:
			length += 1
			count += 1

print(count)