N = int(input())
list1 = list(map(int, input()))     # 숫자의 각 자리수를 list형태로 표현하고 싶을때 12345 [1, 2, 3 ,4, 5]
sum = 0

for i in range(N):
    sum += list1[i]

print(sum)