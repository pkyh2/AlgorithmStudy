def solution(a, b):
    answer = ''
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days = 0

    for i in month.values():
        if a > 1:
            days += i
            a -= 1
            print(days, a)
        else:
            days += b
            break

    days %= 7
    
    answer = week[days-1]
    return answer


a = 5
b = 24
print(solution(a, b))
a = 6
b = 29
print(solution(a, b))
a = 6
b = 1
print(solution(a, b))