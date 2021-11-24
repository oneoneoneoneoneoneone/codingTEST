#큰 수의 법칙 : n개의 숫자 배열에 주어진 수를 m번 더하여 가장 큰 수를 만들되, 연속해서 k번을 초과하여 더할 수 없음
#입력 n m k
#입력 n개의 정수
import time

n, m, k = input().split()   #input().split(' ') : 입력값을 공백기준으로 분리
n = int(n)
m = int(m)  
k = int(k)
s_num = input()
data = []
result, first, second = 0, 0, 0

for i in range(n):
    data.append(int(s_num.split()[i]))


start_time = time.time()                #현재 시간
for i in data:
    if first < i:
        first = i
data.remove(first)
for i in data:
    if second < i:
        second = i

for i in range(m):
    if (i+1) % (k+1) == 0:
        result += second
    else:
        result += first 
end_time = time.time()                  #현재 시간

print(result)
print("내꺼 - ", end_time - start_time)


n, m, k = map(int, input().split())     #공백기준으로 int형 입력
data = list(map(int, input().split()))  #공백기준으로 int형 입력 후 배열로 저장
result = 0

start_time = time.time()                #현재 시간
data.sort()
first = data[n-1]
second = data[n-2]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
end_time = time.time()                  #현재 시간

print(result)
print("남꺼 - ", end_time - start_time)

