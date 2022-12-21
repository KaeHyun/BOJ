# LV1. 햄버거 만들기 

#### 문제 설명:
* 빵 – 야채 – 고기 - 빵 (1,2,3,1) 순서를 찾기 
* 해당 순서를 찾으면 만들 수 있는 햄버거의 개수 증가 


#### 입출력 예시:
|ingredient|result|
|-----|------|
|[2, 1, 1, 2, 3, 1, 2, 3, 1]|2|


-------
``` Python
for burger in ingredient:
        stack.append(burger)
        #print("stack: ",stack)
        #print(stack[-4:])
        
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                stack.pop()
```
>  stack이라는 리스트에 ingredient append
>  만약 뒤에서부터 4개가 [1,2,3,1] 즉, 햄버거를 만들 떄 필요한 재료에 해당한다면, answer의 값을 1 올리고 해당하는 재료들을 pop
>  이때, for문을 range 4로 for문을 돌려주고 pop 진행

-------
* 리스트 슬라이싱 활용의 부족 
