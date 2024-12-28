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
import time
start = time.time()

N = int(input())
temp = N

def primeFactorization(temp):
    if temp != 1:
        if temp <= 3:                                   # 2, 3 일때는 그냥 출력
            print(temp)
        else:
            for i in range(2, temp+1):                  # 2부터 현재 숫자(temp)까지 반복
                if temp % i == 0:                       
                    print(i)                            # 제일 먼저 나눠지는 숫자 출력
                    temp //= i                          # 그 숫자로 현재 숫자(temp)를 나눠주고 다시 temp에 저장 
                    return primeFactorization(temp)     # 반복

    elif temp == 1:                                     # temp가 1이 되면 종료
        return

primeFactorization(temp)

end = time.time()
print(f"{end - start:.5f} sec")

# 시간초가 좀 걸린다...