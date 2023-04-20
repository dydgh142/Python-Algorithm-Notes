def solution(n, m):
    #최대공약수는 1로 설정, 최소공배수는 0으로 설정
    answer = [1,0]
    
    #최대 공약수는 나눈값이 같으며 가장 큰 값을 저장
    for i in range(1, m+1):
        if n%i == 0 and m%i ==0:
            answer[0]=i
            
    # 최소공약수는 두수를 곱한후 최대 공약수르 나눈 값
    answer[1] = n*m //answer[0]
    return answer