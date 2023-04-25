def solution(s, n):
    s = list(s)
    # 초기에 했던 z만 바꾸는 형식은 xy등 뒤에 것들은 포함되지 않기때문에 알파벳 갯수인 26으로 나누고 
    #알파벳 시작인 A or a를 다시 더해 값을 구한다
    for i in range(len(s)) :
        #대문자일떄
        if s[i].isupper() :
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        
        #소문자일때
        elif s[i].islower() :
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            
        # 그외( 공백 )
        else :
            continue
            
    return ''.join(s)