#시각 : 00:00:00 ~ n:59:59 범위의 시각 중 3이 하나라도 포함 되는 경우의 수
#데이터 개수가 100만개 이하일 때 완전탐색 가능
import time

n = int(input())
result = 0

start_time = time.time()                #현재 시간

for i in range(60):
    for j in range(60):
        if str(i).find('3') != -1 or str(j).find('3') != -1:
            result += 1

if n == 23:
    result = result * (n - 2) + (60**2)*3
elif n < 3:
    result = result * (n + 1)
elif n > 12:
    result = result * (n - 1) + (60**2)*2
else:
    result = result * n + 60**2

end_time = time.time()                  #현재 시간

print(result)
print("내꺼 - ", end_time - start_time)


result = 0
start_time = time.time()                #현재 시간

for i in range(n +1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

end_time = time.time()                  #현재 시간

print(result)
print("남꺼 - ", end_time - start_time)