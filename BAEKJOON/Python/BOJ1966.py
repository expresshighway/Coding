message = list(input())
result = ''
flag = True

if '_' in message:
  for i in range(len(message)):
    if message[i] == "_":
      message[i+1] = message[i+1].upper()
      message[i] = ''
else:
  for i in range(len(message)):
    if message[i] == message[i].upper():
      message[i] = '_' + message[i].lower()
      flag = True
    else:
      flag = False
      
if flag == False:
  print("Error!")
else:
  print(''.join(message))
