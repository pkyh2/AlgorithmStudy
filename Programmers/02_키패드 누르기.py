def solution(numbers, hand):
    answer = ''
    padDict = {
        1:[0, 0], 2:[0, 1], 3:[0, 2],
        4:[1, 0], 5:[1, 1], 6:[1, 2],
        7:[2, 0], 8:[2, 1], 9:[2, 2],
        '*':[3, 0], 0:[3, 1], '#':[3, 2]
    }

    posL = padDict['*']
    posR = padDict['#']

    for i in numbers:
        # 왼쪽, 오른쪽 일때
        if i in [1, 4, 7, '*']:
            answer += 'L'
            posL = padDict[i]
        elif i in [3, 6, 9, '#']:
            answer += 'R'
            posR = padDict[i]
        else:
            dis_l = 0
            dis_r = 0
            # zip 함수 병렬 처리
            # 두 점 사이 거리구하는게 핵심!
            for a, b, c in zip(posL, posR, padDict[i]):
                dis_l += abs(a-c)
                dis_r += abs(b-c)

            if dis_l == dis_r:
                if hand == "right":
                    answer += 'R'
                    posR = padDict[i]
                else:
                    answer += 'L'
                    posL = padDict[i]
            else:
                if dis_l > dis_r:
                    answer += 'R'
                    posR = padDict[i]
                else:
                    answer += 'L'
                    posL = padDict[i]
    
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