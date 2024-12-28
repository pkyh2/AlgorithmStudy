# 수 정렬하기 2

# 풀이1(퀵 정렬)
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

# 시간 초과



import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)

# pypy3 207368KB 820ms