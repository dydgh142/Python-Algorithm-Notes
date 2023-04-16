from collections import deque

# DFS
def DFS(graph, v):
    visited = {}
    stack = [v]
    while stack:
        d = stack.pop()
        if d not in visited:
            # setdefault(d) key가 d인 value들에서 key와 value 하나를 인자로 받는 메소드
            visited.setdefault(d)
            stack += reversed(graph[d])
    return visited


# BFS
def BFS(graph, v):
    visited = {}
    deq = deque([v])
    while deq:
        d = deq.popleft()
        if d not in visited:
            visited.setdefault(d)
            deq += graph[d]
    return visited


# 정점, 간선, 시작번호
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

print(*DFS(graph, v))
print(*BFS(graph, v))
