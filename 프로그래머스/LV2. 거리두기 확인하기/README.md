# LV2. 거리두기 확인하기

#### 문제 설명:  
* 대기실은 5 * 5 형태로 총 5개
* 맨해트 거리로 2 이하일 경우 거리두기를 지키지 않은 것에 해당  
  - 파티션 존재 시 허용
* 응시자 ("P"), 빈 자리 ("O"), 파티션 ("X")
* 거리두기를 지켰을 경우 return 1 / 한 명이라도 지키지 않은 경우 return 0 

|places|result|
|-----|----|
|[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]]|[1, 0, 1, 1, 1]|

#### 해결 방법: 
- BFS 이용
- 'O' 

``` Python
start = []
for i in range(5):
  for j in range(5):
    #print(place[i][j])
     if place[i][j] == 'P':
        start.append([i,j]) 
```
start 배열에는 search의 시작점이 되는 'P'의 위치를 찾아 저장 
``` Python
    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for i in range(5)]
        distance = [[0]* 5 for i in range(5)]
        visited[s[0]][s[1]] = 1
```
start 배열에 들어간 'P'의 위치를 deque를 이용해 저장  
visited / distance 배열 생성 후 모두 0으로 초기화 
``` Python
if 0<= nx < 5 and 0<= ny <5 and visited[nx][ny] == 0:
  if place[nx][ny] == 'O':
    queue.append([nx,ny])
    visited[nx][ny] = 1
    distance[nx][ny] = distance[x][y]+1
  if place[nx][ny] == 'P' and distance[x][y] <= 1:
    return 0
return 1
```
'O' 즉, 빈자리인 경우 queue에 추가하고 방문한 것 표시 그리고 거리도 계산 후 저장  
'P' 이고 거리고 1보다 작으면 바로 거리두기를 어긴 경우이므로 0을 return


    
