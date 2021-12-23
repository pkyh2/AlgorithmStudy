# 나이순 정렬

'''
'''

import sys
input = sys.stdin.readline

N = int(input())
member = []
member_number = {}
for i in range(N):
    ageName = list(map(str, input().split()))
    member_number[ageName[1]] = i + 1
    member.append(ageName)

for i in range(len(member)):
    member[i][0] = int(member[i][0])

member.sort()
print(member)
print(member_number)

for i in range(1, len(member)):
    if member[i - 1][0] == member[i][0]:
        if member_number[member[i - 1][1]] > member_number[member[i][1]]:
            member[i - 1], member[i] = member[i], member[i - 1]

for i in range(len(member)):
    print(member[i][0], member[i][1])