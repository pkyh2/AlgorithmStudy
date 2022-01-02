# 괄호

'''
입력한 괄호쌍이 VPS(Vaild PS) 인지 확인
'''

# 풀이1(개수로 접근)
# 1. 괄호를 문자열로 입력받는다.
# 2. stack = list(input()) 스택 생성
# 3. 왼쪽, 오른쪽 괄호를 넣을 list 생성
# 4. stack.pop()연산을 통해 원소들을 꺼낸다.
# 5. 괄호의 방향에 맡에 리스트에 넣어주고 크기를 비교해서 다르면 No, 맞으면 Yess

# "\n" 연산 때문에 안됨.
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     stack = list(input())
#     left_parenthesis = []
#     right_parenthesis = []
#     stack_len = len(stack)
#     for _ in range(stack_len):
#         if stack[len(stack)-1] == '(':
#             left_parenthesis.append(stack.pop())
#         elif stack[len(stack)-1] == ')':
#             right_parenthesis.append(stack.pop())
#     if len(left_parenthesis) == len(right_parenthesis):
#         print("YES")
#     else:
#         print("NO")
# ())(() 를 못푼다.

# 풀이2(스택문제인데 스택으로 해야지!)
# 1. 문자열을 하나씩 스택으로 입력받고 괄호가 완성되면 괄호를 내보낸다.
T = int(input())

def check_VPS(parenthesis):
    stack = []
    for i in parenthesis:
        if i == ')':
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()
        else:
            stack.append(i)
    if len(stack) > 0:
        return 'NO'
    else:
        return 'YES'

for _ in range(T):
    parenthesis = input()
    print(check_VPS(parenthesis))
# 29200 76