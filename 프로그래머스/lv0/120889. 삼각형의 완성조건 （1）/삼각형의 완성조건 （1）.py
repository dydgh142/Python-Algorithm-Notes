def solution(sides):
    sides.sort()
    if sides[2]>=sides[1]+sides[0]:
        return 2
    else:
        return 1