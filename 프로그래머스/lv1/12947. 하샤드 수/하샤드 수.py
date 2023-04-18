def solution(x):
    answer = False
    string=str(x)
    arr=[]
    for i in string:
        arr.append(int(i))
    
    result = sum(arr)
    if x % result==0:
        answer=True
    
    return answer