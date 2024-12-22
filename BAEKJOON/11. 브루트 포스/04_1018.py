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
        for k in range(1, 8):   # 1 ~ 8 번 반복  -> !!!for k in range(y_idx, y_idx + 8):!!!
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
result = []    

for y in range(N - 7):  # 10 - 7 0 1 2   
    for x in range(M - 7): # 13 - 7 0 1 2 3 4
        cnt1 = 0
        cnt2 = 0
        for i in range(y, y+8):
            for j in range(x, x+8):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    if board[i][j] != 'W':
                        cnt1 += 1
                    if board[i][j] != 'B':
                        cnt2 += 1
                else:
                    if board[i][j] != 'B':
                        cnt1 += 1
                    if board[i][j] != 'W':
                        cnt2 += 1
        result.append(min(cnt1, cnt2))


print(min(result))

#29200KB 128ms


# 함수 사용
N, M = map(int, input().split())

# 입력받을 borad 생성
board = [''.join(list(input().split())) for _ in range(N)]

# 변경횟수를 담기위한 리스트
result = []    

def eightXeight(y, x):
    cnt1 = 0
    cnt2 = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                if board[i][j] != 'W':
                    cnt1 += 1
                if board[i][j] != 'B':
                    cnt2 += 1
            else:
                if board[i][j] != 'B':
                    cnt1 += 1
                if board[i][j] != 'W':
                    cnt2 += 1
    return cnt1, cnt2

for y in range(N - 7):  # 10 - 7 0 1 2   
    for x in range(M - 7): # 13 - 7 0 1 2 3 4
        result.append(min(eightXeight(y, x)))


print(min(result))