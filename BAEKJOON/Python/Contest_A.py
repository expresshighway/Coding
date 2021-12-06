import sys
input = sys.stdin.readline

num = input()
length = len(num)
arr = []
endStart = length-2

if (int(num) == 999):
  arr.append('999')
  arr.append('999')
elif (length-1 == 2):
  arr.append(num[0])
  arr.append(num[1])
else:
  # 앞자리 수 출력
  if num[0] == num[2]:
    arr.append(num[0]+num[1])
  elif num[0] == num[3]:
    if int(num[0]) == 9 :
      arr.append(num[0])
    else:
      arr.append(num[0]+num[1]+num[2])
  elif int(num[0]) == int(num[1])-1:
    arr.append(num[0])
  else:
    if int(num[0]) == 9 :
      arr.append(num[0])
    else:
      arr.append(num[0]+num[1]+num[2])
  
  #뒤자리 수 출력
  if num[endStart-1] == num[endStart-3]:
    arr.append(num[endStart-1]+num[endStart])
  elif num[endStart-1] == num[endStart-4]:
    arr.append(num[endStart-2]+num[endStart-1]+num[endStart])
  elif int(num[endStart]) == int(num[endStart-1])+1:
    arr.append(num[endStart])
  else:
    arr.append(num[endStart-2]+num[endStart-1]+num[endStart])
  
print(arr[0]+' '+arr[1])