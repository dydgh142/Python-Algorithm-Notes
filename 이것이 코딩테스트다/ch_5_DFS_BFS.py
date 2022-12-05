##### Depth-First Search /  Breadth-First Search #####

## 기본적인 DFS 예제
# def dfs(graph, v, visited):
#     visited[v] = True
#     print (v , end=' ')
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
# graph = [[],
#          [2,3,8],
#          [1,7],
#          [1,4,5],
#          [3,5],
#          [3,4],
#          [7],
#          [2,6,8],
#          [1,7]
#          ]
#
# visited = [False] * 9
#
# dfs(graph, 1, visited)

## 기본적인 BFS 예제
# from collections import deque
#
#
# def bfs(graph, start, visited):
#     #deque 라이브러리를 이용해 queue 생성, start. 즉 1부터 시작
#     queue = deque([start])
#     #1을 바로 트루 처리
#     visited[start] = True
#
#     while queue:
#         #1을 제거하면서 그래프의 값들 순서대로 처리
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             #숫자가 True 로 방문처리 되어있지 않으면
#             if not visited[i]:
#                 #큐에 삽입하고, 방문처리
#                 queue.append(i)
#                 visited[i] = True
#
# graph = [[],
#          [2, 3, 8],
#          [1, 7],
#          [1, 4, 5],
#          [3, 5],
#          [3, 4],
#          [7],
#          [2, 6, 8],
#          [1, 7]
#          ]
#
# visited = [False] * 9
#
# bfs(graph, 1, visited)

## DFS 예제 1. 아이스크림 만들기
# n, m = map(int, input().split())
#
# graph =[]
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m :
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1,y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1
# print(result)

### 미로 찾기 DFS
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
