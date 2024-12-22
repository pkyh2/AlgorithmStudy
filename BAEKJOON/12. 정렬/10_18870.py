# 좌표 압축

'''
입력 받은 값들을 압축하였을때 숫자가 가장 작고 차이가 가장 작은 형태로 변경하여라
'''

# 풀이1
# 갯수 입력, numbers 리스트에 값 입력
# set변수에 numbers대입 후 list sort로 변경
# 이중 for문으로 기존 list에 sortlist 반복하면서 값이 같으면 sortlist의 index를
# result에 대입

# import sys
# input = sys.stdin.readline

# N = int(input())
# numbers = list(map(int, input().split()))

# setNumbers = list(set(numbers))
# setNumbers.sort()   # -10 -9 2 4

# result = []
# for i in numbers:   # 2 4 -10 4 9
#     print(setNumbers.index(i), end=' ')

# 시간초과
# 시간 복잡도 O(N)

# 풀이2
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

setNumbers = list(set(numbers))
setNumbers.sort()

# dictionary comprehension
numbersDict = {setNumbers[i]: i for i in range(len(setNumbers))}
# {-10: 0, -9: 1, 2: 2, 4: 3}

for i in numbers:
    print(numbersDict[i], end=' ')
# 152724 1900
# 시간 복잡도 O(1)