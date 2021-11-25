# 소인수 분해

'''
정수 N이 주어졌을때, 소인수 분해하는 프로그램을 작성하시오.
'''

# 풀이 1 (재귀함수)
# 1. 정수 N을 입력받는다.
# 2. temp에 N을 대입하고 temp가 1이면 걍 종료
# 3. temp != 1면 range(2, int(temp/2)+1) 까지 반복 -> 마지막 소인수가 출력이 안되서 range(2, temp+1)까지로 변경
# 4. temp과 최소로 나눠지는 수를 출력하고
# 5. 그 나눠지는 수로 temp //= i해서 temp에 다시 저장
# 6. 함수 반복

N = int(input())
temp = N

def primeFactorization(temp):
    if temp != 1:
        if temp <= 3:
            print(temp)
        else:
            for i in range(2, temp+1):
                if temp % i == 0:
                    print(i)
                    temp //= i
                    return primeFactorization(temp)

    elif temp == 1:
        return

primeFactorization(temp)

# 시간초가 좀 걸린다...