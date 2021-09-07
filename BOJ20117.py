# 에러를 찾지 못하는 중 도와줘어
N = int(input())
A = list(map(int, input().split()))
B = sorted(A, reverse=True)

sum = 0
if (len(A)%2 == 0):
  cnt = 0
  mid = int(len(A)/2)

else:
  cnt = 1
  mid = int(len(A)/2)
  
for i in range(len(A)):
  if(B[i] == B[mid]):
    break;
  sum += B[i]
  cnt += 1

print(sum*cnt)