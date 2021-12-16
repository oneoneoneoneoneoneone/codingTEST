#왕실의나이트 : 8X8 평면에서 좌표 (a,1)이 주어질 때, 이동할 수 있는 경우의 수 출력
#이동 방법 - 수평 2, 수직 1 / 수직 2, 수평1
import time

x,y = input()
result = 8

start_time = time.time()                #현재 시간

y = int(y)

if(y < 3 or y > 6):
    result -= 2
if(x < 'c' or x > 'f'):
    result -= 2
if(y < 2 or y > 7):
    result -= 1
if(x < 'b' or x > 'g'):
    result -= 1

end_time = time.time()                  #현재 시간

print(result)
print("내꺼 - ", end_time - start_time)


input_data = input()
result = 0

start_time = time.time()                #현재 시간

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1),(-1, -2),(1, -2),(2, -1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

end_time = time.time()                  #현재 시간

print(result)
print("남꺼 - ", end_time - start_time)
