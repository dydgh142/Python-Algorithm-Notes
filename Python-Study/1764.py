# 듣보잡

## 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다.
# N, M은 500,000 이하의 자연수이다.

n, m = map(int, input().split())

arr1 = []
arr2 = []
# n개의 듣도못한 입력받기
for i in range(n):
    x = input()
    arr1.append(x)
#m 개의 보도 못한 입력받기
for i in range(m):
    y = input()
    arr2.append(y)

# set 집합 연산자를 이용해 글자 하나하나 비교후 리스트로 저장 ['fsdfds', 'fsdfsd']형태로 저장
answer = list(set(arr1) & set(arr2))
print(answer)
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])




