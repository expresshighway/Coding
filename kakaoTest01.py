s = "23four5six7"
num = []
for i in range(0,10): num.append(str(i))
eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i in range(0,10):
  s = s.replace(eng[i], num[i])

answer = int(s)
print(answer) 