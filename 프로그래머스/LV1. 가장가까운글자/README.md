# LV1. 신고결과 받기

#### 문제 설명:
* 각 유저는 한 명씩만 신고 / 횟수 제한 X
* 한 유저를 여러번 신고가 가능하지만 동일한 유저가 한 유저를 여러번 신고하면 1회 신고 처리   
  ex) 유저 "muji"가 "neo"를 3번 신고 -> "neo"의 신고 횟수는 1회
* k번 이상 신고 받으면 그 유저는 정지되며 정지된 유저를 신고한 유저에게 메일 발송

#### 입출력 예시:
|id_list|reports|k|result|
|-----|------|---|----|
|["muzi", "frodo", "apeach", "neo"]|["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]|2|[2,1,1,0]|
|["con", "ryan"]|["ryan con", "ryan con", "ryan con", "ryan con"]|3|[0,0]|

-----

``` Python
dic_report = {id:[] for id in id_list}
```
> 입력받은 id_list 순서대로 key값은 id 그리고 빈 배열을 value로 dic_report를 생성

``` Python
for report in set(reports):
  report = report.split(' ')
  dic_report[report[1]].append(report[0])
```
> set 함수는 중복을 없애준다. 따라서, 입력받은 reports에서 중복되는 값이 있다면 제거해준다.  
> 공백을 기준으로 split해서 report에 저장  
> dic_report[신고당한사람].append(신고한사람)  
> ex) {'muzi': ['apeach'], 'frodo': ['apeach', 'muzi'], 'apeach': [], 'neo': ['frodo', 'muzi']}

``` Python
for key, value in dic_report.items():
  if len(value) >= k:
    for v in value:
      answer[id_list.index(v)] += 1
```
> dic_report를 돌면서 만약 value의 길이가 k의 값보다 같거나 크다면 신고당할 유저  
> id_list에서 신고당한 유저의 index 위치와 같은 answer 리스트의 index 위치를 찾아서 1을 추가 

---------
처음에 set 함수를 알았지만 dictionary를 저렇게 선언할 방법이 생각나지 않아서 set 함수를 쓰지 않고 문제를 해결했다.
결과적으로 for문이 예상보다 많이 사용되어 몇 몇 테스트 케이스에서 타임에러 발생.  
또한, 처음에는 신고한 사람들을 key값으로 신고 당한 사람들을 리스트에 넣고 해결했었는데 그보다 신고 당한 사람을 key값으로 신고한 사람들을 리스트에 추가하고 그 길이를 판단하면 되는 사고 흐름을 놓쳤다.  

**missing points**
  * dictionary 선언
  * key-value 배치
