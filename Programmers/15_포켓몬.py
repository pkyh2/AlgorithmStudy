def solution(nums):
    answer = 0
    pick = len(nums)//2
    ori_nums = len(set(nums))
    if ori_nums >= pick:
        answer = pick
    else:
        answer = ori_nums
    return answer

nums = [3,1,2,3]
print(solution(nums))
nums = [3,3,3,2,2,4]
print(solution(nums))
nums = [3,3,3,2,2,2]
print(solution(nums))