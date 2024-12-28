# N-Queen

'''
N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구해라.

4 x 4
[0,0], [1,2], [3,1] 총 3개 x
[0,0], [1,3], [2,1] 총 3개 x

풀이방법
1. 첫번째 행에서 들어갈 곳을 확인한다.
2. 두번째 행에서 들어갈 곳을 확인한다.
3. 세번째 행에서 들어갈 곳이 없다면 두번째 행에서 다음 칸을 확인
4. 세번째 행에서 들어갈 곳을 확인한다.
5. 네번째 행에서 들어갈 곳을 확인했는데 있으면 결과를 하나 더하고, 없다면 첫번째 행에서 두번째 칸으로 이동
'''

def adjacent(x): # x와 i 가 같으면 행이 같은거 근데 for문을 보면 x와 i가 같을 수가 없다.
    for i in range(x): #인덱스가 행  row[n]값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나  or 대각선이 같으면 false       
            return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
    return True
 
#한줄씩 재귀하며 dfs 실행
 
def dfs(x):
    global result
 
    if x == N:          # 각 행에 N개의 퀸이 들어가면 결과 +1
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            row[x] = i      # x번째 행 i번째 열 [0,2,0,0]
            if adjacent(x): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x + 1)

N = int(input())
row = [0] * N       # index는 행을 뜻하고 원소값은 열을 뜻한다.
result = 0          # 전체 횟수를 입력
dfs(0)              # [0,0]부터 시작
# print(row)
print(result)
