def solution(seoul):
    answer = 0
    for i in seoul:
        if i == "Kim":
            break
        answer += 1
    return "김서방은 " + str(answer )+ "에 있다"