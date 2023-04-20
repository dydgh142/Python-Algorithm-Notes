def solution(n, m):
    answer = [1,0]
    for i in range(1, m+1):
        if n%i == 0 and m%i ==0:
            answer[0]=i
            
    answer[1] = n*m //answer[0]
    return answer