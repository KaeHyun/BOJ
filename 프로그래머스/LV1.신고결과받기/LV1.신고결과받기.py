def solution(id_list, reports, k):
    answer = []

    #clean_report = set(report) #리스트 내 중복 제거 
    
    #answer = [0 for i in range(length)]
    answer = [0] * len(id_list) #이렇게 for문을 안돌고 길이만큼 0으로 초기화

    dic_report = {id:[] for id in id_list}
    print(dic_report)
    
    for report in set(reports):
        report = report.split(' ')
        dic_report[report[1]].append(report[0])

    print(dic_report)

    for key, value in dic_report.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1


    print(answer)