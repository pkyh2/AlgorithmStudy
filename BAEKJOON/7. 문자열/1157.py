'''
1. 단어를 입력받는다.
2. 1부터 26이 있는 list를 만들고, 0이 26개가 있는 list를 만든다.
3. 단어에서 알파벳을 하나씩 반복한다.
4. 한 문자를 아스키 코드로 변형하여 소문자, 대문자 a의 아스키 코드값을 빼주면 몇번째인지 나온다
5. 그러면 그에 해당하는 index의 값을 1 올려준다. 
'''

# 단어 입력받고 1 ~ 26 list 만들고, 0 26개 list만들고
word = input()
alphapet = list(range(26)) # 0 ~ 25
list1 = []
for i in range(26):
    list1.append(0)

for i in word:
    lowerIndex = ord(i) - 97            # ord(c) = 99 -> 99 - 97 = 2
    upperIndex = ord(i) - 65
    if lowerIndex in alphapet:          # 0 ~ 25사이의 숫자면
        list1[lowerIndex] += 1
    elif upperIndex in alphapet:
        list1[upperIndex] += 1

maxAlphapetCount = []
for i in list1:                         
    if i == max(list1):                 # zZa -> max값은 2
        maxAlphapetCount.append(i)

if len(maxAlphapetCount) > 1:           # max값이 여러개면 '?' 출력
    print('?')
else:
    maxAlphapetIndex = list1.index(max(list1))      # max값의 index가 몇번째인지 확인
    print(chr(maxAlphapetIndex + 65))               # 대문자로 변경