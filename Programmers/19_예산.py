def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        else:
            answer += 1

    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))
d = [2,2,3,3]
budget = 10
print(solution(d, budget))