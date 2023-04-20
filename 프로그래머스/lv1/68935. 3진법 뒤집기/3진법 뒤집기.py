def solution(n):
    answer = ''

    # 나누는 값이 1이 될때까지 
    while n >= 1:
        # divmod는 몫과 나머지를 한번에 구해줌 n=몫, rest= 나머지
        n, rest = divmod(n, 3)
        # 나머지를 계속해서 answer에 추가해 구함 
        answer += str(rest) #뒤집어진 3진법이 구해짐

    # 파이썬문법 - 3진수로 있는 answer를 10진수로 바꿔줌
    answer = int(answer, 3)

    return answer