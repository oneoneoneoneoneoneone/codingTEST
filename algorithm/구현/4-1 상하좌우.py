#상하좌우 : n x n 정사각 공간에서 (0,0)에서 출발하여 상하좌우 명령 문자에 의해 도착하게 될 좌표 출력. 단, 좌표값이 -가 되는 명령은 무시
#(x, y)이면 앞에가 가로 아니묘...?
import time

n = int(input())
plans = input().split() #list(map(str, input().split()))

x, y = 1, 1

start_time = time.time()                #현재 시간

for i in plans:
    if(i == 'L' and x > 1):
        x -= 1
    if(i == 'R' and x < n):
        x += 1
    if(i == 'U' and y > 1):
        y -= 1
    if(i == 'D' and y < n):
        y += 1

end_time = time.time()                  #현재 시간

print(x, y)
print("내꺼 - ", end_time - start_time)


x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

start_time = time.time()                #현재 시간

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

    x,y = nx, ny

end_time = time.time()                  #현재 시간

print(x, y)
print("남꺼 - ", end_time - start_time)
