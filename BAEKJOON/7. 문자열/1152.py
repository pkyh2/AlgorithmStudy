'''
1. 문장 입력
2. 입력받은 문장을 반복
3. 공백문자를 만나면 앞뒤를 확인하고 단어가 나오면 cnt증가
4. "    "도 단어
'''

# sentence = input()
# spaceCnt = 1

# # 앞 뒤가 공백이면 제거해준다.
# if sentence[0] == ' ':                # " The first character is a blank "
#     sentence = sentence[1:]
# if sentence[len(sentence) - 1] == ' ':
#     sentence = sentence[:-1]

# for i in range(len(sentence)):
#     if sentence[i] == ' ':
#         if sentence[i+1] == ' ':
#             sentence.replace(sentence[i+1], '')

# print(sentence)

# for i in range(1, len(sentence)):
#     if sentence[0] == ' ':
#         if sentence[i] == ' ' and sentence[i + 1] != ' ':
#             spaceCnt += 1
#     elif sentence[len(sentence)-1] == ' ':
#         continue
#     else:
#         if sentence[i] == ' ' and sentence[i + 1] != ' ':
#             spaceCnt += 1

# print(spaceCnt)
# 공백의 크기가 1이든 3이든 상관이없다. 위의 풀이는 공백을 1개일때만 처리함.


word = input().split()
print(len(word))
