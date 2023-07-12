def solution(food):
    #첫 선수 음식
    temp = ''
    # 2번째 숫자부터 2로 나눈후 temp에 추가 
    # 나눠진 몫의 반은 두번째 선수의 숫자로 간다고 생각
    for i in range(1, len(food)):
        #str을 이용하여 해당 숫자를 반복해 temp에 더해줌
        temp += str(i) * (food[i]//2)
        
    # 첫번째 선수 + 0 + 두번째선수 [첫번째 선수의 뒤집은 숫자]
    return temp + '0' + temp[::-1]