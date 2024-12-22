# 균형잡힌 세상

'''
괄호의 종류가 2개 '[]' '()'
입력된 문자열에 괄호가 제대로 짝지어져 있는지 판단
괄호가 하나도 없는 경우에도 올바르게 짝지어진 경우라고 판단
'.'만 입력받으면 종료
'''

# 풀이1(while)
# 입력된 문자열에서 괄호들만 빼고 다 지운다.
# 스택함수를 통해 짝지어진 괄호인지 판단한다.
# 괄호가 없는 문자열도 처리를 해준다.
# '.'만 입력하면 loop종료
import sys
input = sys.stdin.readline

def balence_world(parenthesis):
    stack = []
    for i in parenthesis:
        if i == ']' or i == ')':
            if len(stack) == 0:
                return 'no'
        else:
            stack.append(i)

        if stack[len(stack)-1] == '(':
            if i == ')':
                stack.pop()
            elif i == ']':
                return 'no'
        elif stack[len(stack)-1] == '[':
            if i == ']':
                stack.pop()
            elif i == ')':
                return 'no'
        elif len(stack) == 0:
            if i == ']' or i == ')':
                return 'no'
        else:
            stack.append(i)
    
    if len(stack) > 0:
        return 'no'
    else:
        return 'yes'

while True:
    sentence = input()
    parenthesis = []
    if sentence[0] == '.':
        break
    else:
        for i in sentence:
            if i == ')' or i == '(' or i == '[' or i == ']':
                parenthesis.append(i)
        print(balence_world(parenthesis))

# 29200 144
# [)]. 반례를 처리 안했었음

# 반복문 수정!
import sys
input = sys.stdin.readline

def balence_world(sentence):
    stack = []
    for i in sentence:
        if i == ')' or i == '(' or i == '[' or i == ']':
            if i == ']' or i == ')':
                if len(stack) == 0:
                    return 'no'
            else:
                stack.append(i)

            if stack[len(stack)-1] == '(':
                if i == ')':
                    stack.pop()
                elif i == ']':
                    return 'no'
            elif stack[len(stack)-1] == '[':
                if i == ']':
                    stack.pop()
                elif i == ')':
                    return 'no'
            elif len(stack) == 0:
                if i == ']' or i == ')':
                    return 'no'
            else:
                stack.append(i)
    
    if len(stack) > 0:
        return 'no'
    else:
        return 'yes'

while True:
    sentence = input()
    parenthesis = []
    if sentence[0] == '.':
        break
    else:
        print(balence_world(sentence))
#30860 116