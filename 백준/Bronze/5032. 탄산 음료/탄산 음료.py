a, b, c = map(int,input().split())

a+=b
result = 0
while True:
    result += (a//c)
    a = a//c + a%c
    if a<c:
        break

print(result)
