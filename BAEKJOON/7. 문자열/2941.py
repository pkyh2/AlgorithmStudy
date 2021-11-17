# 크로아티아 알파벳
'''
1. 문자열을 입력받는다.
2. 크로아티아 알파벳 리스트 생성.
3. 단어 개수를 세어줄 변수 cnt생성
4. 리스트(크로아티아 알파벳)를 반복하면서 리스트의 원소가 문자열에 있는지 확인
5. 있다면 replace함수를 이용해 빈 문자열로 변경
6. cnt를 1증가
7. 문자열의 나머지 원소들의 길이를 cnt에 더해준다.
'''

word = input()
CroatiaAlphapet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
temp = ''
list1 = []


for i in CroatiaAlphapet:
    for j in range(1, len(word)):
        temp = word[j-1] + word[j]      # 문자를 2개씩 반복  abcdefg
        if temp == i:
            list1.append(i)             # 크로아티아 알파벳만 저장


for i in list1:
    word = word.replace(i, "")          # 알파벳만 남기고 제거 abc

print(word)
print(list1)
result = len(word) + len(list1)

print(len(word))

#@@@@@@@@@@@@@@@@@@@@@@@정답@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

word = input()
CroatiaAlphapet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in CroatiaAlphapet:
    if i in word:
        word = word.replace(i, '1')

print(len(word))

#@@@@@@@@@@@@@@@@@@@@@@@정답@@@@@@@@@@@@@@@@@@@@@@@@@@@@@