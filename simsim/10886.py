# 0 = not cute / 1 = cute

N = int(input())
c = 0
nc = 0
for i in range(N):
    a = int(input())
    if a == 1:
        c += 1
    elif a == 0:
        nc += 1

if c > nc:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
