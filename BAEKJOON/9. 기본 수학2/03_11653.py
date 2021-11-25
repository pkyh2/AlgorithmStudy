# 소인수 분해

'''
정수 N이 주어졌을때, 소인수 분해하는 프로그램을 작성하시오.
'''

# 풀이 1
# 1. 정수 N을 입력받는다.
# 2. N이 1이면 걍 종료
# 3. N > 1면 2 ~ int(N/2)+1 까지 반복
# 4. N과 최소로 나눠지는 수로 나누고 몫을 다시 N에 저장
# 5. 나눠지는 수를 리스트에 저장
# 6. N이 소수면 그냥 N을 출력

N = int(input())
temp = N
if temp == 1:
    print('')

minimumPrimeNum = []
for i in range(2, int(temp/2)+1):
    if temp % i == 0:
        minimumPrimeNum.append(i)
        if len(minimumPrimeNum) > 1     # 리스트에 값이 들어가면 들어간 값으로 N을 나눠준 몫을 다시 계산한다.
