# 별 찍기 - 10

'''

*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********

'''

# 풀이1
# *을 문제 모양처럼 생성
# 재귀함수를 통해 문제의 모양을 반복
'''
N = int(input())
list1 = [[0 for i in range(N)] for i in range(N)]
print(list1)
def countingStar1(power):
    for i in range(3):
        if i == 1:
            print('{}{}{}'.format('*', ' ', '*'))
        else:
            print('{}'.format('*'*3))


def countingStar(power):
    for _ in range(int(power/3)):
        print('*'*power)
        print('* *' * int(power/3))
        print('*'*power)
    return countingStar(power - 1)
'''
#countingStar(3)
# 모르겠당..

# 풀이2
# 1. 3 X 3 이차원 리스트를 만든다.
# 2. 함수를 생성하고 인자값(n)이 3일때 2차원 리스트에 ***, * *, ***을 대입
# 3. n을 3으로 나눈 몫을 새로운 변수(new_n)에 저장하고 그 변수를 매개변수로 재귀함수실행
# 3-1. 결국 인자값이 3이 될때까지 함수를 반복해준다.

# 4. 인자값이 3인 함수에서 이제 처음 생성한 2차원 리스트에 하나씩 *을 그려준다.
# 5. 이중 for문 3 x 3에서 index [1][1]인 경우가 아닐때
# 6. 반복문을 new_n까지 반복 => new_n은 결국 한줄에 ***가 몇세트 들어가는지 반복
# 7. list1[i+k][j:j+new_n] 3x3의 다음 위치에 = g[k][:new_n] n==3일때 2차원 리스트를 대입
# 7-1. i=0,1,2 k=0~new_n-1 j=0,1,2 

def countingStar(n):
    DIV3 = n//3                                         # 3으로 나눈 몫 값을 저장
    if n == 3:                                          # 3의 1승으로 별모양 초기화
        board[1] = ['*', ' ', '*']
        board[0][:3] = board[2][:3] = ['*']*3
        return
    
    countingStar(DIV3)                                  # 27 x 27 -> 9 x 9 -> 3 x 3으로 재귀함수 실행
    for i in range(0, n, DIV3):                         # 3 x 3부터 시작 (0, 9, 3)
        for j in range(0, n, DIV3):
            if i != DIV3 or j != DIV3:                  # DIV3 == 3
                for k in range(DIV3):                   # 3번 반복
                    board[i+k][j:j+DIV3] = board[k][:DIV3]  # 핵심!! board[0+0][0:1] = board[0][:1] -> '*'하나
                                                            # board[0+0][1:1+1] = board[0][:1]
                                                            # board[3][3]일때는 건너뛰고 ' '빈칸 그대로


import sys
N = int(sys.stdin.readline())
board = [[' ' for _ in range(N)] for _ in range(N)]     # N X N board생성

countingStar(N)

for i in range(N): 
    for j in range(N): 
        print(board[i][j], end='') 
    print()

#67608KB 2624ms