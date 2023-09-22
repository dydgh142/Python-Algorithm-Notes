n = int(input())

cups=[1,2,3]
for i in range(n):
    a, b = map(int, input().split())
    x = cups.index(a)
    y = cups.index(b)
    
    cups[x], cups[y] = cups[y], cups[x]
print(cups[0])