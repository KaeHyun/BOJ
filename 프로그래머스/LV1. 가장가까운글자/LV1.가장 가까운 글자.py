answer = []
    
def cal(idx, v, s):
    tmp = []
    for i in range(0,idx+1):
        if s[i] == v:
            tmp.append(i)
            if len(tmp) > 1:
                result = tmp[-1] -tmp[-2]
    answer.append(result)
            
    
def solution(s):
    dic = []
    for index, value in enumerate(s):
        if value in dic: #dic에 저장되어있다면
            cal(index, value, s)
        else: #dic이라는 곳에 저장되어있지 않다면
            dic.append(value)
            answer.append(-1)

    return answer

# 모범 풀이 - dictiondary 사용해서 인덱스 별 위치를 계속해서 업데이트 해준 후에 계산하는 방법 사용

# def solution(s):
#     answer = []
#     dic = dict() #딕셔너리 생성
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             print(dic)
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i

#     return answer