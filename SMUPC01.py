array = input()
convert = []

for i in range(0,len(array)):
  convert.append(sum(map(int, str(ord(array[i])))))
  print(convert[i]*array[i]) 