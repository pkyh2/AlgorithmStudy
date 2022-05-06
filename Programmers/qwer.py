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
    # 셋 다 같은 경우
    if ans1 == ans2 == ans3:
        answer = [1,2,3]

    # 두 명만 같은 경우
    elif ans1 == ans2 != ans3:
        if max(ans1, ans2, ans3) == ans3:
            answer = [3]
        else:
            answer = [1,2]
    elif ans1 == ans3 != ans2:
        if max(ans1, ans2, ans3) == ans2:
            answer = [2]
        else:
            answer = [1,2]
    elif ans2 == ans3 != ans2:
        if max(ans1, ans2, ans3) == ans1:
            answer = [1]
        else:
            answer = [2,3]

    # 한명만 같은경우
    else:
        if max(ans1, ans2, ans3) == ans1:
            answer = [1]
        elif max(ans1, ans2, ans3) == ans2:
            answer = [2]
        elif max(ans1, ans2, ans3) == ans3:
            answer = [3]

    return answer


answers = [1,2,3,4,5]
print(solution(answers))
answers = [1,3,2,4,2]
print(solution(answers))
answers = [1,1,1,1,1]
print(solution(answers))
answers = [2,2,2,2,2]
print(solution(answers))
answers = [4,4,4,4,4]
print(solution(answers))
answers = [5,5,5,5,5]
print(solution(answers))