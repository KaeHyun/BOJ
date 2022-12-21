def solution(ingredient):
    answer = 0
    stack = []
    for burger in ingredient:
        stack.append(burger)
        #print("stack: ",stack)
        #print(stack[-4:])
        
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                stack.pop()
            

    return answer
    