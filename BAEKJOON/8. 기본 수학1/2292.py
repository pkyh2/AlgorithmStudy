# 벌집

'''
등비수열 수열 문제 공비가 2고 초항이 6이다. 6*2**(n-1)
따라서 저 식에서 n값을 구해주면 된다.
n = log2**(N/3)
'''
import math

N = int(input())

n = math.log2(N/3)

#정수형(int)로 바꿔주고 2항 부터 시작한 등비수열이니까 1항을 더해준다.
print(int(n) + 1)
print(n)

