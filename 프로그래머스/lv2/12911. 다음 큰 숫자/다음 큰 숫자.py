def check(x):
    # 2진수로 바꿔주는 bin 사용
    binary = bin(x)
    # 2진수로 바꾼후 1 갯수세기
    result = binary.count('1')
    return result

def solution(n):
    # 기준을 n으로 잡고 시작
    answer = n
    # check 함수를 통해 1의 갯수를 구함
    num = check(n)
    while True:
        # answer에 1씩 증가시키며 조건확인
        answer +=1 
        # 조건은 check함수를 통해 2진수로 바꾼 1의갯수 파악
        if int(check(answer)) == num:
            return answer
    