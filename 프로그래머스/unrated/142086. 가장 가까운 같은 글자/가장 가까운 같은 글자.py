def solution(s):
    answer = []
    sword = dict()
    
    for i in range(len(s)):
        if s[i] not in sword:
            answer.append(-1)
        else:
            answer.append(i-sword[s[i]])
        sword[s[i]] = i
        
    return answer