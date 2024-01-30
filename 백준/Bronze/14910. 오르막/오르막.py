n = list(map(int,input().split()))
s = sorted(n)
if n == s:
    print('Good')
else:
    print('Bad')