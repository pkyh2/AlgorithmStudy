T = int(input())

for i in range(T):
    ox = input()
    score = 0
    scoreSum = 0

    for i in ox:
        if i == 'O':
            score += 1
            scoreSum += score
        elif i == 'X':
            score = 0
    
    print(scoreSum)
