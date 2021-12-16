# 체스판 다시 칠하기

'''
M x N크기의 보드에서 8 x 8 을 선택해 체스판 형태로 바꿔야 한다
이 때 8x8을 선택하고 체스판으로 바꾸기 위해 최소한으로 색을 변경해야 하는 횟수를 구하시오.
  
'''

# 풀이1
# 입력 받은 문자열을 하나씩 검사
# 중복되는 문자가 있으면 변경
# 8 * 8을 찾아야 한다.
# 항상 양끝은 다르다
'''
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
'''

M, N = map(int, input().split())

# board = [[x for x in input().split()] for _ in range(M)]
# board = [[x] for x in input().split()]
board = [''.join(list(input().split())) for _ in range(M)]

# 각 문자를 행을 반복하면서 중복되는 문자가 있는지 확인
# 각 4 모퉁이에서 시작할 때를 구현

# 왼위에서 시작 [0][0]
cnt = 0
for i in range(M):
    for j in range(N):
        
        a = board[i][j]
        if board[i][j] == 1:
            print(board[i][j], end='')
    print()

print()
# 오위에서 시작 [0][7]
for i in range(M):
    for j in range(N-1, -1, -1):
        print(board[i][j], end='')
    print()

print()
# 오위에서 시작 [7][0]
for i in range(M-1, -1, -1):
    for j in range(N):
        print(board[i][j], end='')
    print()

print()
# 오위에서 시작 [7][7]
for i in range(M-1, -1, -1):
    for j in range(N-1, -1, -1):
        print(board[i][j], end='')
    print()
'''
8 8
CBWBWBWD
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
EWBWBWBF
'''