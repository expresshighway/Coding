n = input()
num = len(n) - 1

answer = 0
for i in range(num):
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
answer += ((int(n) - (10 ** num)) + 1) * (num + 1)

print(answer)