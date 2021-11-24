from random import randint
import time

array = []
for _ in range(10000):  #범위            # for _ in range(n)     : 수행을 반복하되, 변수 값은 무시
    array.append(randint(1,100))        # for i in range(1, n)  : 1~n 의 숫자를 변수에 대입하여 사용할 때
    
start_time = time.time()                #현재 시간
##
for i in range(len(array)):             #범위
    min_index = i                         #최소값 인덱스
    for j in range(i+1, len(array)):    #최소값 제외 비교 대상 범위
        if array[min_index] > array[j]:
                min_index = j
    array[i], array[min_index] = array[min_index], array[i] #치환
##
end_time = time.time()                  #현재 시간

print("선택정렬 - ", end_time - start_time)


array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
##
array.sort()
##
end_time = time.time()

print("기본정렬 라이브러리 - ", end_time - start_time)