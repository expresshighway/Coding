def bfs():
    queue =[]
    #직사각형의 시작점과 이동 횟수를 넣어준다.
    queue.append((0, Sr, Sc))
    
    #큐가 빌때까지
    while queue:
    	#큐에서 한개씩 빼서 확인한다.
        path, row, col = queue.pop(0)
		
        #문제에서 제시한 도착지점에 도착하면 이동 횟수를 반환
        if row == Fr and col == Fc:
            return path
            
		#이동방향은 아래, 위, 왼쪽, 오른쪽        
        for drow, dcol in [[-1, 0],[1,0],[0,-1],[0,1]]:
            nrow = row + drow
            ncol = col + dcol
			
            #해당 시작점이 맵 밖으로 벗어나는 경우
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
                continue
			
            #직사각형 구속조건
            if not isSatisfied(nrow, ncol):
                continue
			
            #위 두조건을 만족시키지 않으면서 방문하지 않았다면
            if not visited[nrow][ncol]:
                visited[nrow][ncol] = 1 #체크해주고
                queue.append((path+1, nrow, ncol)) #큐에 넣어준다.

    return -1

print(bfs())