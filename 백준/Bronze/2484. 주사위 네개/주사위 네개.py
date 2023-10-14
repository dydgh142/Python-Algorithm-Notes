n = int(input())
prizes=[]
for _ in range(n):
    dice=[0]*6
    prize=0
    a=list(map(int, input().strip().split()))
    for i in a:
        dice[i-1] += 1
    if max(dice) == 4:
        prize = 50000 + 5000 * (dice.index(4) + 1)
    elif max(dice) == 3:
        prize = 10000 + 1000 * (dice.index(3) + 1)
    elif max(dice) == 2 and dice.count(2) == 2:
        prize = 2000 + 500 * (dice.index(2) + 1) + 500 * (dice.index(2, dice.index(2) + 1) + 1)
    elif max(dice) == 2:
        prize = 1000 + 100 * (dice.index(2) + 1)
    else:
        some=0
        for i in range(5,-1,-1):
            if dice[i] ==1:
                some = i
                break
        prize=(some +1) *100
    prizes.append(prize)
print(max(prizes))
