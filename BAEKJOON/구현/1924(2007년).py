x, y = map(int, input().split())

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
datesOf31 = (1, 3, 5, 7, 8, 10, 12)
datesOf30 = (4, 6, 9, 11)
date_count = 0

for i in range(1, x):
    if i in datesOf31:
        date_count += 31
    elif i in datesOf30:
        date_count += 30
    else:
        date_count += 28

date_count += y
date_index = date_count % 7
print(days[date_index])