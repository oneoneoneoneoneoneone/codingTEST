#재귀함수 수행은 스택 자료구조와 동일
#수학적 점화식 : 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현
import time


start_time = time.time()                #현재 시간
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
end_time = time.time()                  #현재 시간
print('반복적 구현 : ', factorial_iterative(100))
print('반복적 구현 시간 : ', end_time - start_time)

start_time = time.time()                #현재 시간
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

end_time = time.time()                  #현재 시간
print('재귀적 구현 : ', factorial_recursive(100))
print('재귀적 구현 시간 : ', end_time - start_time)