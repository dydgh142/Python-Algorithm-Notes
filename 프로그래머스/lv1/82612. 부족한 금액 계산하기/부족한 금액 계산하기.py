def solution(price, money, count):
    answer = 0
    count_price = 0
    for i in range(1,count+1):
        count_price += price * i
    
    if count_price >= money:
        answer = count_price - money
    else:
        answer =0
    

    return answer