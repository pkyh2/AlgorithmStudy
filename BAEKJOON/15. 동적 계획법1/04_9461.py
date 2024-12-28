# 파도반 수열
'''
1,1,1,2,2,3,4,5,7,9
6 3
12 16
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, N+1):
        dp[i] = (dp[i-3] + dp[i-2])
    
    print(dp[N])
    # 30864 72