## DFS 예제 1. 아이스크림 만들기

# n,m 으로 얼음틀 크기 받기
n, m = map(int, input().split())

# 얼음틀 입력받기 2차원배열
graph =[]
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 함수 시작
def dfs(x,y):
    # 입력받은 x,y가 범위 밖이면 False 를 리턴함
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    # 주어진 x,y 좌표가 0 즉 얼음틀에 해당한다면 주변 좌표 모두 검사함
    if graph[x][y] == 0:
        graph[x][y] = 1    # 다시 검사하지않도록 방문한 좌표는 1로 변경
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    #그 외의 0이 아닌, 영역 밖이 아닌 (좌표가 1인) 것은 False 리턴
    return False

result = 0
#모든 좌표 범위를 훑어 true값이 반환되면 결과에 1을 더함
for i in range(n):
    for j in range(m):
        if dfs(i, j):       # dfs(i ,j) 가 true면 
            result += 1
print(result)