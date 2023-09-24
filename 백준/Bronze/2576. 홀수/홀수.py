result = 0
min = 99999999
for i in range(7):
    n = int(input())
    if n % 2 ==1:
        result += n
        if n < min:
            min = n
if result == 0:
    print(-1)
else:
    print(result)
    print(min)