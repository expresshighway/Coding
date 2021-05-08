N, M = map(int, input().split())
campus =[list(map(str, str(input().split()))) for _ in range(N)]
count = 0
for i in range(0,N):
  if 'P' in campus[i]:
    key = campus[i].index('P') 
    if(i==N-1):
      if('X' == campus[i-1][key]) and ('X' == campus[i][key-1]):
        continue
      else:
        count += 1
    else:
      count+=1
       
    # if(i == 0):
    #   if key == 0:
    #     if('X' == campus[i+1][key]) and ('X' == campus[i][key+1]):
    #       continue
    #     else:
    #       count += 1
    #   elif key == M-1:
    #     if('X' == campus[i+1][key]) and ('X' == campus[i][key-1]):
    #       continue
    #     else:
    #       count += 1
    #   else:
    #     if(('X' == campus[i][key-1]) and ('X' == campus[i+1][key]) and ('X' == campus[i][key+1])):
    #         continue
    #     else:
    #       count += 1
    # elif (i == N-1):
    #   if key == 0:
    #     if('X' == campus[i-1][key]) and ('X' == campus[i][key+1]):
    #       continue
    #     else:
    #       count += 1
    #   elif key == M-1:
    #     if('X' == campus[i-1][key]) and ('X' == campus[i][key-1]):
    #       continue
    #     else:
    #       count += 1
    #   else:
    #     if(('X' == campus[i-1][key]) and ('X' == campus[i][key-1]) and ('X' == campus[i][key+1])):
    #         continue
    #     else:
    #       count += 1

if(count == 0):
  print('TT')
else:
  print(count)