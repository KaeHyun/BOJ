import re 

def solution(new_id):
    answer = ''
    
    #step 1) 대문 -> 소문자
    new_id = new_id.lower()
    #step 2) 불필요한 문자 제거
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)
    #step 3 & 4) 마침표 2번 이상 -> 1번으로 치환
    new_id = re.sub(r"[\.]{2,}",".", new_id)
    #new_id = new_id.replace("..",".")
    if new_id.strip()[-1] == "." or new_id.strip()[0] ==".":
        new_id = new_id.strip(".")
    #step 5 ) 빈 문자열이라면 
    if not new_id:
        new_id = "a"
    #step 6)
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip(".")
    #step 7)
    if len(new_id) < 3:
        word = new_id.strip()[-1]
        #print(word)
        while(True):
            new_id = new_id + word
            if len(new_id) == 3: break;
    answer = new_id
    return answer