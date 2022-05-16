from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    
    
    return sorted(list(answer))

numbers = [2,1,3,4,1]
print(solution(numbers))