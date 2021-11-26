# 거스름돈 문제 : 거슬러줄 돈이 n일 때 동전의 최소 개수
# for문으로 화폐 종류의 수만큼 반복, 시간복잡도 = O(K)
import time

n = 1260
count = 0
coin_types = [500, 100, 50, 10]

start_time = time.time()                #현재 시간
for coin in coin_types :
    count += int(n/coin)
    n %= coin
end_time = time.time()                  #현재 시간

print("총 동전의 수 : ", count)
print("내꺼 - ", end_time - start_time)


n = 1260
count = 0
coin_types = [500, 100, 50, 10]

start_time = time.time()                #현재 시간
for coin in coin_types:
    count += n // coin                  # // :나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    n %= coin
end_time = time.time()                  #현재 시간
    
print("총 동전의 수 : ", count)
print("남꺼 - ", end_time - start_time)
