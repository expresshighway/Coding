import sys

input = sys.stdin.readline
N, M = map(int, input().split())

MAP = []
for _ in range(N):
    row = list(map(int, input().split()))
    MAP.append(row)

H, W, Sr, Sc, Fr, Fc = map(int, input().split())

#좌표 시작 기준점이 1,1 이므로 1씩 빼준다. 
Sr, Sc, Fr, Fc = Sr-1, Sc-1, Fr-1, Fc-1 

#발견 여부를 기록할 리스트
visited = [[0 for i in range(M)] for i in range(N)]

#직사각형 내부에 벽이 있으면 안되므로 벽 위치를 기록해준다.
walls =[]
for row in range(N):
    for col in range(M):
        if MAP[row][col] ==1:
            walls.append((row,col,))
            
#새롭게 이동된 시작으로 직사각형이 움직일 수 있는지 없는지를 판단
def isSatisfied(nrow, ncol):
	
    #이동한 시작점을 기준으로 했을 때 직사각형이 맵 밖으로 넘어가면 안된다.
    if nrow + H -1 >= N or ncol + W -1 >= M:
        return False

	#직사각형 내부에 벽이 있으면 안된다.
    for w_row, w_col in walls:
        if nrow <= w_row < nrow + H and ncol <= w_col < ncol + W:
            return False
    return True


#BFS
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