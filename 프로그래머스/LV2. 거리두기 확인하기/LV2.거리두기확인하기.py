from collections import deque

def bfs(place):
                
    dx = [-1,1,0,0] #좌우
    dy = [0,0,1,-1] #상하 

    start = []
    for i in range(5):
        for j in range(5):
            #print(place[i][j])
            if place[i][j] == 'P':
                start.append([i,j]) #시작점이 되는 'p'의 좌표를 찾아 start 배열에 그 좌표를 저장
    #print(start)

    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for i in range(5)]
        distance = [[0]* 5 for i in range(5)]
        visited[s[0]][s[1]] = 1 #start 지점에 저장된 부분은 방문한 것으로 check
        
        #print(visited)

        while queue:
            x,y = queue.popleft()
            #print("y: " + str(y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < 5 and 0<= ny <5 and visited[nx][ny] == 0:
                    if place[nx][ny] == 'O':
                        queue.append([nx,ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y]+1
                    
                    if place[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1



def solution(places):
    answer = []
    for i in places:
        #print(i)
        answer.append(bfs(i))
    
    print(answer)

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])

