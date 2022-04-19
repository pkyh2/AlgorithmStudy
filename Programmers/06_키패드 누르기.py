from numpy import number


def solution(numbers, hand):
    answer = ''
    keyPad = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    posL = 3
    posR = 3
    for i in numbers:
        for j in range(len(keyPad)):
            if i in keyPad[j]:
                if j == 0:
                    if i == keyPad[j][0]:
                        answer += 'L'
                        posL = 0
                    elif i == keyPad[j][2]:
                        answer += 'R'
                        posR = 0
                    else:
                        if posL == posR:
                            if hand == "right":
                                answer += 'R'
                            else:
                                answer += 'L'
                        elif abs(posL-j) < abs(posR-j):
                            answer += 'L'
                        else:
                            answer += 'R'
                    break
                elif j == 1:
                    if i == keyPad[j][0]:
                        answer += 'L'
                        posL = 1
                    elif i == keyPad[j][2]:
                        answer += 'R'
                        posR = 1
                    else:
                        if posL == posR:
                            if hand == "right":
                                answer += 'R'
                            else:
                                answer += 'L'
                        elif abs(posL-j) < abs(posR-j):
                            answer += 'L'
                        else:
                            answer += 'R'
                    break
                elif j == 2:
                    if i == keyPad[j][0]:
                        answer += 'L'
                        posL = 2
                    elif i == keyPad[j][2]:
                        answer += 'R'
                        posR = 2
                    else:
                        if posL == posR:
                            if hand == "right":
                                answer += 'R'
                            else:
                                answer += 'L'
                        elif abs(posL-j) < abs(posR-j):
                            answer += 'L'
                        else:
                            answer += 'R'
                    break
                else:
                    if i == keyPad[j][0]:
                        answer += 'L'
                        posL = 2
                    elif i == keyPad[j][2]:
                        answer += 'R'
                        posR = 2
                    else:
                        if posL == posR:
                            if hand == "right":
                                answer += 'R'
                            else:
                                answer += 'L'
                        elif abs(posL-j) < abs(posR-j):
                            answer += 'L'
                        else:
                            answer += 'R'
                    break
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"	
print(solution(numbers, hand))