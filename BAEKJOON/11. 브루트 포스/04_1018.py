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
        if board[i][j] == 'W':
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

# 풀이2
# 8 x 8의 board를 만들고
# board를 옮겨 가면서
# 변경 횟수가 가장 적은 숫자를 출력
'''
N, M = map(int, input().split())

# 입력받을 borad 생성
board = [''.join(list(input().split())) for _ in range(M)]

# 변경횟수를 담기위한 리스트
result = []

for y_idx in range(N - 7):      # 0 1
    for x_idx in range(M - 7):
        cnt = 0
        for k in range(1, 8):   # 1 ~ 8 번 반복
            for l in range(1, 8):
                if board[y_idx + k - 1][x_idx + l - 1] == 'B':
                    if (x_idx + k) % 2 == 0 and:
                        if board[y_idx + k - 1][x_idx + l] != 'W':
                            cnt += 1
                    if board[y_idx + k][x_idx + l - 1] != 'W':
                        cnt += 1
                # i=0, j=0, k 1~8, l 1~8
                elif board[y_idx + k - 1][x_idx + l - 1] == 'W':
                    if board[y_idx + k - 1][x_idx + l] != 'B':
                        cnt += 1
                    if board[y_idx + k][x_idx + l - 1] != 'B':
                        cnt += 1
                
            print(cnt)
            result.append(cnt)

print(result)
'''

N, M = map(int, input().split())

# 입력받을 borad 생성
board = [''.join(list(input().split())) for _ in range(N)]

# 변경횟수를 담기위한 리스트
result_min = []

def check_8x8(board, str, row, col):
    cnt_W = 0
    cnt_B = 0
    result = []
    if str == 'W':
        for i in range(8):
            for j in range(8):
                if ((col + i) % 2 == 0 and (row + i) % 2 == 0) or ((col + i) % 2 == 1 and (row + i) % 2 == 1):
                    if board[col + i][row + j] != 'W':
                        cnt_W += 1
                elif ((col + i) % 2 == 0 and (row + i) % 2 == 0) or ((col + i) % 2 == 1 and (row + i) % 2 == 1):
                    if board[col + i][row + j] != 'B':
                        cnt_W += 1
    if str == 'B':
        for i in range(8):
            for j in range(8):
                if ((col + i) % 2 == 0 and (row + i) % 2 == 0) or ((col + i) % 2 == 1 and (row + i) % 2 == 1):
                    if board[col + i][row + j] != 'W':
                        cnt_B += 1
                elif ((col + i) % 2 == 0 and (row + i) % 2 == 0) or ((col + i) % 2 == 1 and (row + i) % 2 == 1):
                    if board[col + i][row + j] != 'B':
                        cnt_B += 1
    result.append(cnt_W)
    result.append(cnt_B)

    return result
        
for i in range(N - 7):  # 10 - 7 0 1 2   
    for j in range(M - 7): # 13 - 7 0 1 2 3 4
        if board[i][j] == 'B':
            result_min.append(min(check_8x8(board, 'B', j, i)))
        elif board[i][j] == 'W':
            result_min.append(min(check_8x8(board, 'B', j, i)))

print(result_min)