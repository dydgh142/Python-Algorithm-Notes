def solution(s):
    answer = s 
    num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    # num_s의 키-값 을 item으로 가져와서 사용
    for item in num_s.items():
        answer = answer.replace(item[0], str(item[1]))   


    return int(answer)