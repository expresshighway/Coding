arr = ['무지', '콘', '어피치', '제이지', '프로도', '네오', '튜브', '라이언']
k=2
n = len(arr)
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
copy = arr[:]
del_num = []
del_list = []
answer = []
global store
cnt = 0

for i in range(len(cmd)):
  if "U" in cmd[i]:
    x, y = cmd[i].split() 
    k = k - int(y)
    # print(copy[k])
  elif "D" in cmd[i]:
    x, y = cmd[i].split()
    k = k + int(y)
    # print(copy[k])
  elif "C" in cmd[i]:
    store = k
    if store == (len(arr)-1):
      k = 0
    del_num.append(store)
    del_list.append(copy[store])
    del copy[store]

  elif "Z" in cmd[i]:
    copy.insert(del_num.pop(), del_list.pop())
    # print(copy[k])

for i in range(len(arr)):
  if arr[i] in copy:
    answer.append('O')
  else:
    answer.append('X')

answer = ''.join(answer)
print(answer)