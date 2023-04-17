def solution(n, words):
    answer = [words[0]]
    result =[0,0]

    for i in range(1, len(words)):
        if answer[-1][-1] == words[i][0] and words[i] not in answer:
            answer.append(words[i])
        else :
            result[0] = (i%n) +1
            result[1] = i//n+1
            break
            
    return result
    