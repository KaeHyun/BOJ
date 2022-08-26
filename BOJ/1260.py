#DFS와 BFS

#Python은 기본적으로 문자로 입력을 받는다.
#공백으로 들어오는 정수 입력 각각 입력받기 
# N : 정점의 개수 / M : 간선의 개수 / V :  탐색을 시작할 정점의 번호

N,M,V = map(int, input().split())

#인접 행렬 생성 / 정점의 개수 만큼 
graph = [[0]*(N+1) for i in range(N+1)]

# 방문 체크
visited = [0]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# print(graph)

def DFS(V):
    visited[V] = 1 #방문한 곳은 1로 체크
    print(V, end =' ')

    for i in range(1, N+1):
        #방문한 적이 없고 인접한 행렬에 간선이 존재한다면 재귀함수로 다시 DFS 
        if(visited[i] == 0 and graph[V][i] ==1): 
            DFS(i)


def BFS(V):
    q = [V] #방문할 곳을 순서대로 큐에 저장
    visited[V] = 0 #DFS를 먼저 실행했으므로 V는 다시 0으로 방문 체크

    while q: #빈 큐가 될때까지 
        V = q.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited[i] == 1 and graph[V][i] == 1):
                q.append(i)
                visited[i] = 0


DFS(V)
print()
BFS(V)


