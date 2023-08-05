def solution(a, b, n):
    answer = 0
    while a <= n:
        r = n % a #빈병으로 받을 수 있는 콜라수 r
        n = (n//a) * b # 받는 콜라수 n
        answer += n #합산
        n += r # 남아있는 병 한번씩 더해주기
    return answer