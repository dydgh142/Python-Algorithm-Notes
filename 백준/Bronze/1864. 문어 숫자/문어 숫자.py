count_dict = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while 1:
    s = input()
    if s == '#':
        break
    num = 0
    for i in range(len(s)):
        num += count_dict[s[i]] * 8**(len(s)-i-1)
    print(num)