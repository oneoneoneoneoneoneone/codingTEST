#DFS(Depth-First Search) : 깊이 우선 탐색
#스택 자료구조 (재귀 함수) / O(N) 시간 소요

def dfs(graph, v, visited):
    visited[v] = True  #방문
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:  #인접노드가 false이면 수행
            dfs(graph, i ,visited)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9   #false로 초기화
dfs(graph, 1, visited)