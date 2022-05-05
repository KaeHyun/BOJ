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
