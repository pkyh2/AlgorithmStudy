def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

def solution(numbers):
    return 45 - sum(numbers)
    
numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))
numbers = [5,8,4,0,6,7,9]
print(solution(numbers))