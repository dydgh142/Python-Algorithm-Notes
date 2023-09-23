n = int(input())
cnt = 1
count = 0
while n >0:
    if n < cnt:
        cnt = 1
    n -= cnt
    cnt += 1
    count += 1

print(count)


