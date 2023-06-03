def solution(answers):
    list1=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    list2=[2, 1, 2, 3, 2, 4, 2, 5]
    list3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answers[i] == list1[i % len(list1)]:
            score[0] += 1
        if answers[i] == list2[i % len(list2)]:
            score[1] += 1
        if answers[i] == list3[i % len(list3)]:
            score[2] += 1
        
    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)
            
    return answer