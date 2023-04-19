def solution(s):
    answer = ''
    if len(s)==1:
        return s
    
    half = len(s)//2 
    # 3->1 4->2 5->2  6->3 7->3
    if len(s)%2==1:
        answer = s[half]
    else:
        answer = s[half-1]+ s[half]
        
    
    return answer