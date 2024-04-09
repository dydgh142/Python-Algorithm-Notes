import sys

s = sys.stdin.read()
a = [0] * 26

for i in s:
    if i.islower():
        a[ord(i)-97] += 1

for j in range(26):
    if a[j] == max(a):
        print(chr(97+j), end='')