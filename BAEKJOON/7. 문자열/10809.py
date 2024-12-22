# find(찾을 문자, 찾기 시작할 위치) -> 찾는문자의 index값을 알려준다.
# 찾는 문자가 없을 경우 -1을 리턴
# S = 'abcdefghi'
# S.find('a') -> 0
# S.find('a', 4) -> -1
# S.find('d', 2) -> 3

S = input()
alphapet = list(range(97, 123)) # 97 ~ 122

for i in alphapet:
    print(S.find(chr(i)), end=' ') # chr(97) -> a