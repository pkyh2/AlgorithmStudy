# 01타일

'''
N이 짝수일때는 1도 무조건 짝수개
홀수일때는 1이 홀수개

N == 1, 1
N == 2, 2
N == 3, 3
N == 4, 5
'''
import sys
input = sys.stdin.readline

N = int(input())
dp =[0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[N])
# 69396 396