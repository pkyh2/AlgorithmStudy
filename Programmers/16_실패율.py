def solution(N, stages):
    clear = { key:0 for key in range(1, N+1) }
    for i in stages:
        for j in clear.keys():
            if i == j:
                clear[j] += 1
    clear = sorted(clear.items(), key=lambda x: x[0])

    fail = {}
    challenger = len(stages)    # 8
    for i in clear:
        fail[i[0]] = i[1]/challenger
        challenger -= i[1]

    fail = list(map(lambda x: x[0], sorted(fail.items(), key = lambda x: float(x[1]), reverse=True)))
    
    return fail

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))

# 1, 6, 7, 9, 13, 23, 24, 25 런타임 에러