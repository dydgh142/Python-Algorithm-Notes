def solution(arr):
    answer = []
    for i in arr:
        if i >=50 and i%2==0:
            answer.append(i//2)
            continue
        if i < 50 and i%2==1:
            answer.append(i*2)
            continue
        answer.append(i)
    return answer