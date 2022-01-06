#게임개발 : nXm 평면에서 좌표 (a,b)와 방향 d, 맵을 입력받아, 방문한 칸의 수 출력
#왼쪽 방향의 칸이 가보지 않은 칸이면 왼쪽으로 회전 후 전진, 가본 칸이면 회전 후 재수행. 네 방향 가보거나 바다인 경우 후진 후 재수행. 뒤칸이 바다인경우 멈춤
#3 <= n / m <= 50 / d - 0,1,2,3(북,동,남,서) / 맵 - 0,1(육지,바다)
import time

n,m = map(int, input().split())
a,b,d = map(int, input().split())
m = []
result = 1

for _ in range(n):
    _m = list(map(int, input().split()))
    m.append(_m)

start_time = time.time()                #현재 시간

d = 3 if d==0 else d-1                  #3항 연산자 : true if 조건 else false
while (True) :
    if(m[a-1][b] != 0 and m[a+1][b] != 0 and m[a][b-1] != 0 and m[a][b+1] != 0):
        if(d == 0):
            if(m[a+1][b] == 1):
                break
            else:
                a +=1
        elif(d == 1):
            if(m[a][b-1] == 1):
                break
            else:
                b -=1
        elif(d == 2):
            if(m[a-1][b] == 1):
                break
            else:
                a -=1
        elif(d == 3):
            if(m[a][b+1] == 1):
                break
            else:
                b +=1
    else:
        if(d == 3 or d == -1):
            if(m[a+1][b] == 0):
                #d = 0
                m[a][b] = 2
                a += 1
                result+=1
            else:
                d -= 1
        elif(d == 2):
            if(m[a-1][b] == 0):
                #d = 0
                m[a][b] = 2
                a -= 1
                result+=1
            else:
                d -= 1
        elif(d == 1):
            if(m[a][b+1] == 0):
                #d = 0
                m[a][b] = 2
                b += 1
                result+=1
            else:
                d -= 1
        elif(d == 0):
            if(m[a][b-1] == 0):
                #d = 0
                m[a][b] = 2
                b -= 1
                result+=1
            else:
                d += 3


end_time = time.time()                  #현재 시간

print(result)
print("내꺼 - ", end_time - start_time)


n,m = map(int, input().split())
d = [[0]*m for _ in range(n)]
a,b,direction = map(int, input().split())
d[a][b] = 1 #현재좌표 방문처리

m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

start_time = time.time()                #현재 시간

#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = b + dx[direction]
    ny = a + dy[direction]
    #이동
    if d[nx][ny] == 0 and m[nx][ny] == 0:
        d[nx][ny] = 1
        b= nx
        a= ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = b - dx[direction]
        ny = a - dy[direction]

        if m[nx][ny] == 0:
            b = nx
            a = ny
        
        else:
            break
        turn_time = 0


end_time = time.time()                  #현재 시간

print(count)
print("남꺼 - ", end_time - start_time)
