def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5] * (10000 // 5)
    supo2 = [2,1,2,3,2,4,2,5] * (10000 // 8)
    supo3 = [3,3,1,1,2,2,4,4,5,5] * (10000 // 10)

    ans1, ans2, ans3 = 0, 0, 0
    
    for i, sp1, sp2, sp3 in zip(answers, supo1, supo2, supo3):
        if i == sp1:
            ans1 += 1
        if i == sp2:
            ans2 += 1
        if i == sp3:
            ans3 += 1

    k = max(ans1, ans2, ans3)
    if k == ans1:
        answer.append(1)
    if k == ans2:
        answer.append(2)
    if k == ans3:
        answer.append(3)

    return answer

answers = [1,2,3,4,5]
print(solution(answers))
answers = [1,3,2,4,2]
print(solution(answers))