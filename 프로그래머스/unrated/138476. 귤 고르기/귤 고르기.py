def solution(k, tangerine):
    answer=0
    dict1 = {}
    # 딕셔너리를 이용하여 무게별 귤의 갯수를 넣음
    for i in tangerine:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    # dict2에는 갯수가 많은 순서대로 정렬하기
    dict2 = sorted(dict1.items(), key=lambda x: -x[1])
    # lambda : x는 -x[1] 의 위치를 기준으로 내림차순 정렬한다. 
    
    # 가장많은 갯수의 귤부터 채워나가 몇종류의 귤이 들어갔는지 카운트하기 
    for i in dict2:
        if k <= 0:
            break
        else:
            k -= i[1]
            answer += 1
    return answer