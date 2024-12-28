# 하노이 탑 이동 순서

'''
한 번에 한 개의 원판만 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
첫째줄에 횟수를 입력하고 그 아래 수행 과정을 출력한다.
'''

# 풀이1
# 쌓인 원판의 개수 입력
# 1. N개의 원판 리스트 생성
# 2. 장대의 3개의 리스트 생성
# 3. 1번째 원판을 마지막번째 장대로 옮김
# 4. 2번째 원판을 2번째 장대로 옮김
# 5. 1번째 원판을 1장대 2장대의 수를 비교해서 작은 쪽으로
# 6. 1번 장대를 맨 마지막으로
# 7. 1, 3을 비교해서 1이 더 크면 2번을 1번으로
# 8. 그리고 남은 원판을 3번으로

N = int(input())

board1 = [i for i in range(N, 0, -1)]     # 1~N까지 생성
board2 = []
board3 = []
print('0단계')
print(board1)
print(board2)
print(board3)


# 1단계
board3.append(board1.pop(len(board1)-1))
board2.append(board1.pop(len(board1)-1))

print('1단계')
print(board1)
print(board2)
print(board3)

# 2단계
board2.append(board3.pop(len(board3)-1))
board3.append(board1.pop(len(board1)-1))


print('2단계')
print(board1)
print(board2)
print(board3)

# 3단계
board1.append(board2.pop(len(board2)-1))
board3.append(board2.pop(len(board2)-1))
board3.append(board1.pop(len(board1)-1))
print('3단계')
print(board1)
print(board2)
print(board3)

# 4단계
board2.append(board1.pop(len(board1)-1))
board2.append(board3.pop(len(board3)-1))
board1.append(board3.pop(len(board3)-1))
board1.append(board2.pop(len(board2)-1))
board2.append(board3.pop(len(board3)-1))
board3.append(board1.pop(len(board1)-1))
board2.append(board1.pop(len(board1)-1))
board2.append(board3.pop(len(board3)-1))

print('4단계')
print(board1)
print(board2)
print(board3)


# 풀이2 재귀
import sys
def hanoi(num, start, end, assist):
    if num == 1:
        print(start, end)
        return
    
    hanoi(num-1, start, assist, end)    # n-1개를 assist로
    print(start, end)                   # n번 판을 end로
    hanoi(num-1, assist, end, start)    # n-1개를 assist(원래 start)로

N = int(sys.stdin.readline())
print(2**N - 1)                         # 하노이 탑의 일반항 
hanoi(N, 1, 3, 2)

#29452KB 876ms