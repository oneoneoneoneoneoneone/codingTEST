#BFS(Breadth-First Search) : 너비 우선 탐색 (가까운 노드부터 탐색)
#큐 자료구조 / O(N) 시간 소요
#수행시간 BFS < DFS (성능? BFS > DFS)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True   #방문
    
    while queue:
        v = queue.popleft()
        print(v, end= ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9   #false로 초기화
bfs(graph, 1, visited)