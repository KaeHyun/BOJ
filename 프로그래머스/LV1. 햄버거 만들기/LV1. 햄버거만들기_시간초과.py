def check(ham_str, ing_str, answer):
    flag = 0
    while(flag == 0):
        if ham_str in ing_str:
            ing_str = ing_str.replace(ham_str, "")
            answer = answer+1
        else: flag = 1
    return answer
def solution(ingredient):
    #햄버거 순서 1,2,3,1
    hamburger = [1,2,3,1]
    answer = 0

    ham_str = ''.join(str(s) for s in hamburger)
    ing_str = ''.join(str(s) for s in ingredient)
    
    print(check(ham_str, ing_str, answer))
    return check(ham_str, ing_str, answer)

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])