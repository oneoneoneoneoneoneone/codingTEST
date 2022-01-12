#    [노드]
#    /   \   <--(간선)
#[노드]  [노드]

#그래프 표현 방식
#인접 행렬(Adjacency Matrix) : 2차원 배열로 연결 관계 표현
#인접 리스트(Adjacency List) : 리스트로 연결 관계 표현
#속도 - 행렬 > 리스트 / 메모리 - 리스트 > 행렬

INF = 999999999 #무한의 비용 선언
#인접행렬 - 2차원 리스트로 표현
graph = [[0,2,3],[2,0,INF],[3,INF,0]]

print(graph)


#파이썬 리스트 자료형 : 배열 + 연결리스트(append() 메소드)

#인접 리스트 - 행이 n개인 2차원 리스트
graph = [[] for _ in range(3)]
#노드 0에 연결 된 노드 정보(노드, 거리)
graph[0].append((1,2))
graph[0].append((2,3))
graph[1].append((0,2))
graph[2].append((0,3))

print(graph)