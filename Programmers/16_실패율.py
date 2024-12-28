def solution(N, stages):
    # 1부터 N까지 key값으로하고 value가 0인 dict 초기화
    clear = { key:0 for key in range(1, N+1) }
    # 시간복잡도 O(n**2) 각 stage별 clear수 체크
    for i in stages:
        for j in clear.keys():
            if i == j:
                clear[j] += 1
    # dict -> list, tuple 형태로 변경
    clear = sorted(clear.items(), key=lambda x: x[0])

    fail = {}
    challenger = len(stages)    # 8
    # 각 stage별 실패율 계산
    for i in clear:
        if challenger == 0:
            fail[i[0]] = 0
        else:
            fail[i[0]] = i[1]/challenger
        challenger -= i[1]

    # fail dict에서 value별로 정렬하고, 해당 key값만 list로 반환
    fail = list(map(lambda x: x[0], sorted(fail.items(), key = lambda x: float(x[1]), reverse=True)))
    
    return fail

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))

# 1, 6, 7, 9, 13, 23, 24, 25 런타임 에러 -> challenger가 0일때 추가로 해결!