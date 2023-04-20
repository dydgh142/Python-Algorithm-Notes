def solution(arr):
    b = []
    for i in range(len(arr)):
        #첫번째 항목은 무조건 추가
        if i == 0:
            b.append(arr[i])
        #두번째부터는 바로 이전항목과 비교해서 같지않으면 추가
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b