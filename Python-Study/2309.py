# 일곱 난쟁이

# 아홉명의 난쟁이중 7명의 진짜 난쟁이를 찾아내기
# 7명의 키를 더하면 100이 됨.

# 여러 개 입력 받을 리스트
a = []
for i in range(9):
    a.append(int(input().rstrip()))

for j in a:
    for k in a:
        if sum(a) - j - k == 100 and j != k:
            a.remove(j)
            a.remove(k)

a.sort()
for i in a:
    print(i)
