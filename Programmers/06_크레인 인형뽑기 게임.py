'''
1. N x N 격자형
2. 크레인이 인형을 집으면 빈 바구니에 채워넣는다.
3. 동일한 인형이 연속으로 2개가 담기면 사라진다.(stack)
4. 크레인(crane)이 인형이 없는곳에 간 경우는 아무일도 일어나지 않는다.
5. 인형뽑기 board와 크레인의 작동위치 moves가 담긴 배열이 주어진다.
6. 크레인을 모두 작동시킨 후 사라진 인형의 개수(answer)를 구하시오.
'''



def solution(board, moves):
    answer = 0
    basket = []
    # 크레인
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                # 바구니의 마지막 숫자와 뽑은 인형의 숫자가 같으면
                if basket and board[j][i-1] == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
            else:
                continue

                    
    return answer

# board[0][0], board[4][4]
board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))