def solution(arr):
    answer = []
    result = []
    
    if len(arr) <= 1:
        answer.append(-1)
        
    min_value= min(arr)
    for i in arr:
        if i != min_value:
            answer.append(i)
            
    return answer