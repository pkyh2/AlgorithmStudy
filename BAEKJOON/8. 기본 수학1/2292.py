# 벌집

# 계차수열 문제였다.
'''
1, 7, 19, 37, 61, 91...
등차가 일정하지 않고 6, 12, 18, 24, 30...으로 증가한다.
일반항은
1 + 6*0
1 + 6*1
1 + 6*3
1 + 6*6
이런 식이다.
이 식의 일반항을 구해야 한다.
=> 1 + 3n(n - 1)
n값의 정수형을 구하면 정답이다.
'''
# 외부 모듈 사용 X
'''
import sympy as sym

N = int(input())
n = sym.symbols('n')
ans = sym.solve(3*n**2 - 3*n + 1 - N, n)
print(int(ans[1])+1)
'''

N = int(input())
honeycomb = 1       # 벌집의 개수 1개부터 시작
cnt = 1             # 증가
while N > honeycomb:    # 입력한 번호의 벌집이 현재 벌집개수보다 크면 반복
    honeycomb += 6*cnt  # 벌집개수가 6의 배수만큼 증가
    cnt += 1
print(cnt)