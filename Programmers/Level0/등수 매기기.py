def solution(score):
    answer = []
    s_score = [sum(i) for i in score]
    s_score.sort(reverse=True)
    
    rank, cnt = 1, 0
    ranking = {}

    for i in range(len(score)):
        if (ranking):
            if s_score[i-1] == s_score[i]:
                ranking[s_score[i]] = rank
                cnt += 1
            else:
                rank += 1+cnt
                cnt = 0
                ranking[s_score[i]] = rank
        else:
            ranking[s_score[i]] = rank

    for i in score:
        answer.append(ranking.get(sum(i)))
    return answer

score = [[80, 70], [90, 50], [40, 70], [50, 80]]
print(solution(score))
score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))