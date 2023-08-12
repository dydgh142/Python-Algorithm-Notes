def solution(elements):
    length = len(elements)
    #중복되지 않게 모든 수열의 합을 더해줄 sum_all
    sum_all = set()

    # 길이만큼 반복
    for i in range(length):
        # sum_all 에 elements[i]를 담음
        ssum = elements[i] 
        sum_all.add(ssum)
        # i 다음숫자부터 길이가 달라지는 부분수열을 모두 더해 넣음
        for j in range(i+1, i+length):
            ssum += elements[j%length] #현재 시작점 값 + elements[] 값을 ssum에 더함
            # print("j%length : ", j%length, "ssum : ", ssum)
            sum_all.add(ssum)
    return len(sum_all)
    
#     answer = 0
#     #합의 종류를 구분하는곳
#     sum_all = set()
    
#     #length는 1 ~ elements의 갯수
#     for length in range(1, len(elements)+1):
#         # 처음부터 시작하는곳을 하나씩 더해줌
#         for i in range(len(elements)):
#             temp = 0    #temp는 이번 길이의 수를 더하는 용도
#             j = i       #j는 길이의 수
#             k = 0       # k는 마지막 지점을 파악하는 용도
#             while k < length:
#                 if j >= len(elements):
#                     j=0
#                 temp += elements[j]
#                 j += 1
#                 k += 1
#             #합의 종류가 포함되지 않는다면 answer+=1
#             if temp not in sum_all:
#                 answer+=1
                
    