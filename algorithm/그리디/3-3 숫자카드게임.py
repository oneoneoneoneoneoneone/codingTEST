#숫자 카드 게임 : n x m 행렬에 임의의 행에서 가장 낮은 숫자만 선택할 수 있을 때 선택할 수 있는 가장 높은 숫자
#
import time

n, m = map(int, input().split())
card = []
result = 0

start_time = time.time()                #현재 시간
for _ in range(n):
    data = list(map(int, input().split()))
    card.append(min(data))

result = max(card)
end_time = time.time()                  #현재 시간

print(result)
print("내꺼 - ", end_time - start_time)


result = 0

start_time = time.time()                #현재 시간
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)
end_time = time.time()                  #현재 시간

print(result)
print("남꺼(2중 반복문) - ", end_time - start_time)
    
