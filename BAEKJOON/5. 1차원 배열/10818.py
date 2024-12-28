# N = int(input())
# list1 = list(map(int, input().split()))

# minNum = list1[0]
# for i in range(1, N):
#     if minNum > list1[i]:
#         minNum = list1[i]

# maxNum = list1[0]
# for i in range(1, N):
#     if maxNum < list1[i]:
#         maxNum = list1[i]

# print('{} {}'.format(minNum, maxNum))


N = int(input())
list1 = list(map(int, input().split()))

for i in range(N):
    if list1[i] == min(list1):
        minNum = min(list1)
    if list1[i] == max(list1):
        maxNum = max(list1)

print('{} {}'.format(minNum, maxNum))