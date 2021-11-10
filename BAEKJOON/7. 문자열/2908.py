'''
1. 두 수를 입력받는다.
2.
3. 두 수를 다시 비교한다.
'''

A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)