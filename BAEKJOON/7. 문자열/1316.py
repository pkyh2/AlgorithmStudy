# 그룹 단어 체커

N = int(input())
cnt = 0

def wordProcessing(word):
    list1 = []
    for i in range(0, len(word)-1):
        temp = ''
        if word[i] == word[i+1]:
            temp += word[i]
        else:
            list1.append(temp)
        


for i in range(N):
    word = input()
    list1 = []
    temp = ''
