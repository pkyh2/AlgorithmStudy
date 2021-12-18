# 수 정렬하기 2

import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)

def quick_sort(array, start, end):
    if start >= end:
        return
    
    #피벗, 왼쪽, 오른쪽 값 설정
    pivot = start
    left = start + 1
    right = end

    #반복하면서 left right 값찾아서 swap
    while(left <= right):
        while(left <= end and numbers[pivot] >= numbers[left]):     # pivot보다 작으니까 반복
            left += 1
        while(numbers[pivot] <= numbers[right] and right > start):
            right -= 1
        if left > right:
            numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    # 왼쪽 그룹, 오른쪽 그룹도 정렬 수행
    quick_sort(numbers, start, right - 1)
    quick_sort(numbers, right + 1, end)

        


quick_sort(numbers, 0, len(numbers)-1)
for i in numbers:
    print(i)



import sys

N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)

# 생성된 원소에서 최대값 크기의 배열 선언
count = [0] * (max(numbers) + 1)

# 생성한 배열의 길이만큼 반복하면서 count배열에 생성배열 원소에 해당하는 index값을 1증가함
for i in range(len(numbers)):
    count[numbers[i]] += 1

# count 배열의 길이만큼 반복하면서 
for i in range(len(count)):
    #count배열의 원소개수가 원래 배열의 개수니까 그만큼 반복하면서 원래 원소를 출력
    for j in range(count[i]):
        print(i)


N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)

#207368KB 820ms