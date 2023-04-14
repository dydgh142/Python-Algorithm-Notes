# 큐를 이용하기 위한 deque 가져오기
from collections import deque

#n 과 m 을 공백을 이용하여 받고
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 지도 값을 받음

# 상하좌우로 움직일 값들
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    #초기값으로 넘어온 값들을 queue에 추가해 놓고
    queue.append((x, y))

    #큐가 없어질때까지 무한반복
    while queue:
        # 제일 초기값을 제거후 주변 상하좌우 를 대입해 최초로 방문하는 곳을 찾음
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나거나 0 인곳은 무시함
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            # 1인곳을 최초로 방문한다면 현재 값 + 1 을 해줌으로 최단경로 값을 더해나감
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 처음 입력받은 지도 크기만큼 마지막값이 왔을때 반환함
    return graph[n - 1][m - 1]

# 가장 처음 위치를 대입하여 bfs 함수 시작
print(bfs(0, 0))
