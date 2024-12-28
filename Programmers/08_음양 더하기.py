def solution(absolutes, signs):
    answer = 0
    for i in zip(absolutes, signs):
        if i[1] == False:
            answer -= i[0]
        else:
            answer += i[0]
    return answer

absolutes = [4,7,12]
signs = [True, False, True]
print(solution(absolutes, signs))