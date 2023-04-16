def solution(order):
    result = 0
    for i in str(order):
        if i in ["3","6","9"]:
            result += 1
    
    return result