def solution(arr):
    answer = 0
    result =0 
    for i in arr:
        result += i
    
    answer = result/len(arr)
    return answer