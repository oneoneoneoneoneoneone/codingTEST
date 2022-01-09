#오버플로 : 수용가능한 데이터 크기 이상의 삽입연산을 수행할 때 발생
#언더플로 : 데이터가 없는 상태에서 삭제연산을 수행할 때 발생
#list 자료형 *append() : 뒤 삽입 *pop() : 뒤 삭제

stack = []

stack.append(1)
stack.append(2)
stack.pop()
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop()

print(stack)
print(stack[::-1])  #최상단 원소부터 출력


from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.popleft()
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()

print(queue)        #먼저 들어온 원소부터 출력
queue.reverse()     #역순 정렬
print(list(queue))