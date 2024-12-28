# 분수찾기

'''
1 - 1/1
2 - 1/2
3 - 2/1
4 - 3/1
5 - 2/2
6 - 1/3
7 - 1/4
8 - 2/3
9 - 3/2
'''

N = int(input())    # 입력번호
group = 1
row = 1

# N이 몇번째 행인지
while N > group:
    row += 1                # 행
    group += row            # N행 까지의 전체 분수 개수

# 해당 행의 분수들을 넣어둠
list1 = []
for i in range(1, row+1):   # 각 행을 반복
    numerator = row+1-i     # 분자 row, row-1, ... 4, 3, 2, 1
    denominator = i         # 분모 1, 2, 3, 4, ...
    fraction = str(numerator) + '/' + str(denominator)
    list1.append(fraction)

# 행이 홀수행 짝수행을 구분하여 각 행의 첫번째 시작 번호를 구하고
# 홀수행은 순서대로, 짝수행은 역순으로 원소가 들어있어서
# 홀수행은 입력한 숫자에서 첫번째 숫자를 뺀 값이 입력한 숫자의 위치에 있는 index여서 list1에서 해당 원소를 출력한다. 
if row % 2 == 1:    # 홀수 행이면
    a1 = 3          # 초항
    cd = 4          # cd(common difference) 공차
    n = int(row//2)      # n항
    ap = a1 + (n - 1)*4     # ap(arithmetic progression) 등차수열
    row_first_num = (n*(a1 + ap)) // 2 + 1    # 등차수열의 합 + 1 -> 행의 첫번째 숫자
    print(list1[N - row_first_num])

# 짝수행은 반대로 첫번째 숫자에서 입력한 숫자를 빼면 index값이 나온다.
else:
    a1 = 7
    cd = 4
    n = int(row//2) - 1
    ap = a1 + (n - 1)*4
    row_last_num = (n*(a1 + ap)) // 2 + 3 # 등차수열의 합 + 맨앞 숫자(3) -> 행의 마지막 숫자
    print(list1[row_last_num - N])

'''
각 행의 차이가 등차수열을 이루는 계차수열
따라서 그 x행의 첫번째 숫자는 = (등차수열들의 합과 1행의 첫번째 숫자를 더한 값이다.) 40, 49번째줄 
'''