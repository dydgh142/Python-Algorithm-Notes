def ap(n):
    # 1~99
    if n < 100:
        return n

    # 100~999
    elif n < 1000:
        cnt = 99
        for i in range(100, n + 1):
            i = str(i)
            a, b, c = int(i[0]), int(i[1]), int(i[2])
            if ((a + c) / 2) == b:
                cnt += 1
        return cnt
    else:
        return ap(999)


x = int(input())
print(ap(x))
