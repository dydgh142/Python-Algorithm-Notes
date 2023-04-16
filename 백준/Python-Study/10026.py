# 적록색약

## 범위에서 일반인과 적록색약 사람이 보는 구분갯수를 구하라
from collections import deque
from turtledemo.planet_and_moon import G

# 움직여지는 좌표
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())        #n 크기의 정수값

#입력 값을 전부 리스트 형태로 받아야함.
#[['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'],
# ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'],
# ['R', 'R', 'R', 'R', 'R']]

a = []
for i in range(n):
    a.append(list(map(str, input())))
#visited = c
c = [[0] * n for _ in range(n)]
q = deque()

print(a)
def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        #방문한 곳 삭제
        x, y = q.popleft()
        #양방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #방문하지 않은곳. 추가하고 그곳으로 이동
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == a[x][y] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1




cnt1 = 0
for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            a[i][j] = 'G'
c = [[0] * n for _ in range(n)]

cnt2 = 0
for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            cnt2 += 1
print(cnt1, cnt2)
