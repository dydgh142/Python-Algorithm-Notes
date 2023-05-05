def solution(s):
    stack=[]
    
    for i in s:
        # 초기값(비교할 값) 스택에 추가
        if len(stack)==0:
            stack.append(i)
        #스택의 제일 마지막 값과 현재 값이 같다면, 제거 
        elif stack[-1] == i:
            stack.pop()
        #스택에 추가
        else:
            stack.append(i)
            
    return 1 if len(stack)==0 else 0