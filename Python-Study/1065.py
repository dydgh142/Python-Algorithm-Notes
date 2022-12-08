# 1065
## 한수

###
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
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
