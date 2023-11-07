cnt = int(input())

for _ in range(cnt) :
  n, m = map(int, input().split())
  u = (m*2) - n
  cnt = n - m
  print(u, cnt)