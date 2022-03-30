def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    minRank = 0
    for i in win_nums:
        for j in lottos:
            if i == j:
                minRank += 1

    maxRank = minRank + lottos.count(0)
    if minRank > 1:
        for num, ranking in rank.items():
            if maxRank == num:
                answer.append(rank[num])
            if minRank == num:
                answer.append(rank[num])
    else:

    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
lottos = [0, 0, 0, 0, 0, 0]	
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))
lottos = [45, 4, 35, 20, 3, 9]	
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))

