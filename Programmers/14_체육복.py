def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _lost = [i for i in lost if i not in reserve]
    _reserve = [j for j in reserve if j not in lost]
    
    for j in _reserve:
        b = j-1
        f = j+1
        if b in _lost:
            _lost.remove(b)
        elif f in _lost:
            _lost.remove(f)
            
    answer = n - len(_lost)
    return answer


# n = 5
# lost = [2,4]
# reserve = [1,3,5]
# print(solution(n, lost, reserve))
# n = 5
# lost = [2,4]
# reserve = [3]
# print(solution(n, lost, reserve))
# n = 3
# lost = [3]
# reserve = [1]
# print(solution(n, lost, reserve))
n = 5
lost = [1,4]
reserve = [2,3,4,5]
print(solution(n, lost, reserve))