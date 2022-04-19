def solution1(L, x):
    answer = []
    if x not in L:
        answer.append(-1)
    else:
        for i in range(len(L)):
            if L[i] == x:
                answer.append(i)
    return answer

L = [64, 72, 83, 72, 54]
x = 72
print(solution1(L, x))
L = [64, 72, 83, 72, 54]
x = 83
print(solution1(L, x))
L = [64, 72, 83, 72, 54]
x = 49
print(solution1(L, x))