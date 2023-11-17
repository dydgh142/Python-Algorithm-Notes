def solution(numbers):
    n = len(numbers)
    stack = [0]
    answer = [-1] * n
    
    for i in range(1,n):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer