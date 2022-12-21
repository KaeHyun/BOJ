# LV1. 가장 가까운 같은 글자 찾기

#### 문제 설명:
* 처음 나온 글자는 -1
* 처음 나오지 않은 글자는 가장 가까운 같은 글자를 찾아 거리 계산

#### 입출력 예시:
|s|result|
|-----|------|
|"banana"|[-1, -1, -1, 2, 2, 2]|
|"footbar"|[-1, -1, 1, -1, -1, -1]|

-----

``` Python
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            print(dic)
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
```
>  dictiondary 사용해서 인덱스 별 위치를 계속해서 업데이트 해준 후에 계산하는 방법 사용

``` Python
def cal(idx, v, s):
    tmp = []
    for i in range(0,idx+1):
        if s[i] == v:
            tmp.append(i)
            if len(tmp) > 1:
                result = tmp[-1] -tmp[-2]
    answer.append(result)
```
> 나는 거리계산 함수 만들어서 for문 2번 사용 -> 비효율적


**missing points**
  * dictionary 활용

