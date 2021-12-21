# 단어 정렬

'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다. -> set사용
'''
# 풀이1
import sys

N = int(sys.stdin.readline())

words = set()
for i in range(N):
    word = input()
    words.add(word)

words = list(words)
words.sort()

result = []
for i in words:
    words_tuple = (len(i), i)
    result.append(words_tuple)

result.sort()

for i in range(len(result)):
    print(result[i][1])

# 33812 896