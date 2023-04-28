def solution(my_string):
    answer = ''
    alist=['a','e','i','o','u']
    for i in my_string:
        if i in alist:
            continue
        answer += i
    return answer