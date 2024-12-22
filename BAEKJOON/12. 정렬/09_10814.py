# 나이순 정렬

'''
'''

import sys
input = sys.stdin.readline

# N = int(input())
# member = []
# member_number = {}
# for i in range(N):
#     ageName = list(map(str, input().split()))
#     member_number[ageName[1]] = i + 1
#     member.append(ageName)

# for i in range(len(member)):
#     member[i][0] = int(member[i][0])

# member.sort()
# print(member)
# print(member_number)

# for i in range(1, len(member)):
#     if member[i - 1][0] == member[i][0]:
#         if member_number[member[i - 1][1]] > member_number[member[i][1]]:
#             member[i - 1], member[i] = member[i], member[i - 1]

# for i in range(len(member)):
#     print(member[i][0], member[i][1])


# 풀이2

N = int(input())

members = []

for i in range(N):
    members.append(list(input().split()))

print(members)

# member의 원소값['21', 'Junkyu']에서 0번째 원소를 int로 바꿔 그 기준으로 sort
members.sort(key=lambda a : int(a[0]))

for i in range(N):
    print(members[i][0], members[i][1])

# 51764 4220