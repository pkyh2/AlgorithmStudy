'''
다이얼 1은 2초
        2는 3초 ... 4는 5초
ex) ABC면 3초, 
'''

alphapet = input()
list1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in alphapet:
    for j in list1:
        if i in j:
            result += list1.index(j) + 3

print(result)