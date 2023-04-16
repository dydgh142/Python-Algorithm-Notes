def solution(n):

    a = list(str(n))
    a.sort(reverse=True)
    n = int("".join(a))
    return n