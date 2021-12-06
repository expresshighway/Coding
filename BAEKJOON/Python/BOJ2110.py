import sys

N, C = map(int, input().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

# 라우터 간격을 얼마나 해야할지 모르니 최대거리와 최소거리의 중간부터 시작
left = 1
right = house[-1] - house[0]
answer = 0
while right >= left:
    # 중간값
    mid = (right + left) // 2
    # 라우터 설치
    count = 1
    before_install = house[0]
    for i in range(1, N):
        if house[i] >= before_install + mid:
            count += 1
            before_install = house[i]
    if count < C:
        right = mid - 1 # 와이파이 개수가 C보다 작으면 더 설치해야 한다. 간격을 좁히자.
    else:
        left = mid + 1 # 와이파이 개수가 C보다 많거나 같으면 덜 설치해야 한다. 간격을 넓히자.
        # 중간에 mid를 저장하는 이유는 개수를 만족할 때 간격을 늘리려다가 개수를 만족시키지 못하고 while문이 종료될 수 있다.
        answer = mid

print(answer)
 