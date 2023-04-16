# 올림픽               8점 나중에 다시 풀어보기
## 등수계산하기

### 첫번째 줄에 국가 갯수, 순위를 알고싶은 나라 순서번호

#a - 국가 갯수, b - 알고싶은 나라
a, b = map(int, input().split())
k = []
result = 0
for i in range(a):
    #리스트에 리스트로 입력받아 2차배열로 받음
    k.append(list(map(int, input().split())))
# k[i]의 오름차순으로 정렬
k.sort()
for i in range(a):
    #알고 싶은 나라의 순서를 result에 입력
    if k[i][0] == b:
        result = i

for i in range(a):
    #알고싶은나라의 순서와 정렬한 후 순서에 맞는 나라가 매달 갯수가 같다면  출력
    if k[result][1:] == k[i][1:]:
        print(i + 1)
        break

