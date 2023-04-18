def solution(numbers):
    answer = -1
    arr = [1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        if i in arr:
            arr.remove(i)
    answer = sum(arr)
    return answer