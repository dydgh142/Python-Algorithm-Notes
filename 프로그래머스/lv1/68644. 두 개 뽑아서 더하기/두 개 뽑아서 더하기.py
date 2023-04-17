def solution(numbers):
    # 정답배열
    answer = []
    
    # 입력받은 것들의 더하는 경우를 모두 answer에 추가 
    for i in range(len(numbers)):
        for r in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[r])
    
    #중복제거, 리스트화 한 후 정렬
    answer=list(set(answer))
    answer.sort()
    
    return answer