def solution(t, p):
    answer = 0
    
    # p의 크기를 쉽게 변수에 담아둠
    p_len = len(p)
    
    # t길이에서 p길이만큼 뺀 후 돌려야 오류가 나지 않음
    for i in range(len(t)-p_len+1):
        # t에서 p의 길이만큼 비교를 했을때 p보다 작거나 같은것이 있으면 +=1
        if int(t[i:i+p_len]) <= int(p):
            answer += 1
    return answer