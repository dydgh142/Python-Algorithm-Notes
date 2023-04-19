def solution(s):
    answer = ''
    s=list(str(s))
    s.sort(reverse=True)
    answer+=''.join(s)

    return answer