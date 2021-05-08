n = int(input())
array =[list(map(int, input().split())) for _ in range(n)]
rank = []

for i in range(n):
    num = 1;
    for j in range(n):
        if(array[i][0] < array[j][0]) and array[i][1] < array[j][1]: # 몸무게 크고 키도 크면
            num =  num+1
    rank.append(num)

for i in rank:
    print(i, end=' ') 