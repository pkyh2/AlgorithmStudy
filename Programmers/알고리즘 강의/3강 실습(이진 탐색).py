def solution(L, x):
    start = 0
    end = len(L)-1
    while start <= end:
        middle = (start + end)//2
        # 탐색을 끝까지했는데도 값이 존재하지 않는 경우
        if (end-start)==2 and L[middle] != x:
            if L[start] == x:
                return start
            elif L[end] == x:
                return end
            else:
                return -1
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            start = middle
        else:
            end = middle


L = [2, 3, 5, 6, 9, 11, 15]
x = 6
print(solution(L, x))
L = [2, 5, 7, 9, 11]
x = 4
print(solution(L, x))
L = [1, 2, 3]
x = 3
print(solution(L, x))