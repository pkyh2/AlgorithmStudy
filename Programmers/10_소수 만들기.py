from itertools import combinations

def primeNum(num):
    for i in range(2, int(num**0.5)+1):
        if i > 1:
            if num % i == 0:
                return False  
    return True

def solution(nums):
    answer = sum(map(lambda x: primeNum(sum(x)), combinations(nums, 3)))
    return answer

nums = [1,2,3,4]
print(solution(nums))
nums = [1,2,7,6,4]
print(solution(nums))