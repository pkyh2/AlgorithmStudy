def solution1(x):
    f0, f1 = 0, 1

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        for _ in range(2, x+1):
            fi = f0 + f1
            f0 = f1
            f1 = fi
        return fi

def solution2(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution2(x-1) + solution2(x-2)

print(solution1(9))
print(solution2(9))