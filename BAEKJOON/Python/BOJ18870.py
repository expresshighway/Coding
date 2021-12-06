import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

Y= sorted(list(set(X)))
# answer = []
# for i in range(N):
#   cnt = 0
#   for j in range(N):
#     if(X[i] == Y[j]):
#       break;
#     cnt += 1;
#   print(cnt, end=" ")

Y = {Y[i]:i for i in range(len(Y))}
print(*[Y[i] for i in X])