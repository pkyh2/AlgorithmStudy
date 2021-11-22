# 소수 찾기

'''
주어진 수 N개 중에서 소수가 몇 개인지 찾는 문제
소수 : 1과 자기 자신으로만 나눠지는 수
'''

# 풀이 1
# 1. 몇개의 수를 입력할지 N을 입력받는다
# 2. N번 수를 입력하고 리스트에 저장한다.
# 3. cnt변수를 만들어 소수면 cnt를 증가한다.

N = int(input())
list1 = list(map(int, input().split()))

if 1 in list1:
    list1.remove(1)

for i in list1:
    print(i)
    for j in range(2, i):
        print(j)
        if i % j == 0 and i in list1:
            list1.remove(i)

print(len(list1))
print(list1)