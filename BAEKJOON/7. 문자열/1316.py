# 그룹 단어 체커
# aaabbbccca
'''
N = int(input())
cnt = 0

def wordProcessing(word):
    list1 = []
    for i in range(0, len(word)-1):
        temp = ''
        if word[i] == word[i+1]:    #앞뒤가 같으면 temp에 저장
            temp += word[i]         # 여기서 += 가 아니라 그냥 대입으로 했었어야했다.
                                    # 그리고 리스트에 해당 단어 저장하고 나중에 또 나오면 그룹단어가 아닌걸로하는 방식으로 하면 좋겠다.
        else:
            list1.append(temp)
        


for i in range(N):
    word = input()
    list1 = []
    temp = ''
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
N = int(input())

def groupChecker(word):
    alphaList = []
    for j in range(1, len(word)):
        if word[j-1] != word[j]:                # aabbcccb 에서 ab가 같지 않으니까
            alphaList.append(word[j-1])         # 빈 리스트에 a추가
            if word[j-1] in alphaList:          # 뒤에 알파벳이 앞에서 들어가 있는 알파벳에 속해있으면 return 0 -> 이게 문제!
                return 0
            else:
                return 1 
        print(alphaList)

for i in range(N):
    #alphapet = list(map(chr, range(97, 123)))   # a ~ z 알파벳 리스트 생성
    word = input()                              # 단어 입력
    cnt = 0
    if groupChecker(word) == 1:
        cnt += 1

    print(cnt)
'''

#@@@@@@@@@@@@정답@@@@@@@@@@@@
'''
find() 변수.find(찾을문자) -> 그 문자의 처음 index값이 나온다.(중복 상관없이 처음 index)
따라서 aabbcccb에서
a의 index는 0 b는2 c는4 인데 뒤에 또 b가 2가 나왔으니까
앞뒤 문자를 비교해서 앞의 문자의 index값이 큰경우가 뒤에 앞에 반복되는 문자가 또 나온다는 얘기
'''

N = int(input())
count = N

for _ in range(N):  #반복할 수가 필요없을때는 빈칸으로 둬도된다.
    word = input()

    for i in range(len(word)-1): # happy word[0] ~ word[3] word.find('h') -> 0 word.find(word[1]) -> 
        if word.find(word[i]) > word.find(word[i+1]):   # ex) happy h:0 a:1 p:2 y:3  /  happhy p:2 h:0 -> x
            count -= 1
            break
print(count)


#@@@@@@@다른사람풀이@@@@@@@@

banbock = int(input())      #개수 입력
txt = []                    # 빈 리스트 생성
for i in range(banbock):    # 입력한 개수만큼 반복
    txt.append(input())     # 빈 리스트에 입력한 단어들을 저장 ex) ['happy', 'new', 'year']

group_word = 0              
for t in txt:               # 리스트에서 각 단어를 하나씩 반복
    pre_char = ''           # 빈 문자 선언
    used_char = [0] * 26    # 0이 26개 있는 리스트 선언
    for i in range(len(t)):     # 단어의 길이만큼 반복 ex) happy 0, 5
        if pre_char != t[i]:    # 단어의 원소가 빈 문자가 아니면
            used_char[ord(t[i])-ord('a')] += 1  # 0이 26개 있는 리스트에 단어의 아스키 숫자값에 a 97값을 빼준다 = 단어의 위치에 1을 더해준다.
                                                # ex) h 면 7번 index값에 1을 더해준다.
        pre_char = t[i]         # 같으면 그냥 단어에 대입

    if max(used_char) == 1:     # 만약 1씩 더한 리스트에서 max값이 1이면 그룹단어이므로 1을 더해준다.
        group_word += 1

print(group_word)