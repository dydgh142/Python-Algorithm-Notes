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
