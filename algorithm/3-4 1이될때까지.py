#1이 될 때까지 : n이 1이 될때까지 두 연산 중 하나를 선택하여 반복할 때 최소 연산 횟수 (2번은 n % k 가 0일 때만 수행 가능)
# 1. n - 1 
# 2. n / k
# 내가 이김 ><

import time

n, k = map(int, input().split())
result = 0

start_time = time.time()                #현재 시간

while(True):
    result += 1

    if(n % k == 0):
        n = n / k
    else:
        n -= 1
    if(n == 1):
        break

end_time = time.time()                  #현재 시간

print(result)
print("내꺼 - ", end_time - start_time)


n, k = map(int, input().split())
result = 0

start_time = time.time()                #현재 시간

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n-= 1
    result += 1

end_time = time.time()                  #현재 시간

print(result)
print("남꺼 - ", end_time - start_time)


result = 0

n, k = map(int, input().split())
start_time = time.time()                #현재 시간

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n -1)

end_time = time.time()                  #현재 시간

print(result)
print("남꺼2 - ", end_time - start_time)