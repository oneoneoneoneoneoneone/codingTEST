#큰 수의 법칙 : n개의 숫자 배열에 주어진 수를 m번 더하여 가장 큰 수를 만들되, 연속해서 k번을 초과하여 더할 수 없음
#입력 n m k
#입력 n개의 정수
import time

n, m, k = map(int, input().split())     #공백기준으로 int형 입력
data = list(map(int, input().split()))  #공백기준으로 int형 입력 후 배열로 저장
result = 0

start_time = time.time()                #현재 시간
data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result += (count) * first
result += (m - count) * second
end_time = time.time()                  #현재 시간

print(result)
print("남꺼2 - ", end_time - start_time)


result = 0

start_time = time.time()                #현재 시간
data.sort()
first = data[n-1]
second = data[n-2]

result += int(m/(k+1)) * (first * k + second) + first * (m % (k+1))
end_time = time.time()                  #현재 시간

print(result)
print("내꺼2 - ", end_time - start_time)
