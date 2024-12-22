# 수 정렬하기

# 풀이1(삽입정렬)
# 맨앞의 수가 정렬되어 있다고 생각하고 2번째 수부터 이전 숫자와 비교하여 크기 순서대로 변경한다.
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

for i in range(1, len(numbers)):
    for j in range(i, 0, -1):
        if numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
        else:
            break

for i in numbers:
    print(i)

# 29200 288

# 풀이2(퀵정렬)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

def quick_sort(numbers, start, end):
    if start >= end:	# numbers의 원소가 1개인 경우 종료
        return
    pivot = start		# pivot는 0번째 원소
    left = start + 1	# 왼쪽 방향
    right = end			# 오른쪽 방향
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and numbers[left] <= numbers[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and numbers[right] >= numbers[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:	# 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            numbers[left], numbers[right] = numbers[right], numbers[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(numbers, start, right - 1)
    quick_sort(numbers, right + 1, end)
    
quick_sort(numbers, 0, len(numbers) - 1)

for i in numbers:
    print(i)

# 29960 116