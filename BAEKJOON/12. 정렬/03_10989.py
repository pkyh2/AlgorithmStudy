# 수 정렬하기3

'''
계수정렬 사용
입력받은 수들 중에서 가장 큰 값을 길이로 하는 리스트를 생성
입력받은에 대응하는 index값의 개수를 하나씩 증가
index에 해당하는 값의 개수만큼 index를 출력
'''
# 풀이1 (계수정렬)
import sys
input = sys.stdin.readline

N = int(input())


index_list = [0] * 10001
for i in range(N):
    num = int(input())
    index_list[num] += 1

for i in range(len(index_list)):
    for j in range(index_list[i]):
        print(i)

# 29708 8980