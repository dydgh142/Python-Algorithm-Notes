# 차이를 최대로

## N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서
# 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

##|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

all = permutations(a)
ans = 0

for i in all:
    s = 0
    for j in range(1, n):
        s += abs(i[j] - i[j - 1])
    if ans < s:
        ans = s
print(ans)