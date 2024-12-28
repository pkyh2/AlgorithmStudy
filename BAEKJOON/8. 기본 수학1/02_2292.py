# 벌집

# 풀이 1
# 계차수열로 접근
'''
1, 7, 19, 37, 61, 91... 각 칸의 맨 마지막 수
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
# 계차수열을 이용해서는 외부모듈을 사용할 수 없기 때문에 해결할 수 없다.
# 따라서 
N = int(input())    # 벌집의 번호 입력
honeycomb = 1       # 1마을의 벌집의 개수
cnt = 1             # 몇번째 방인지
while N > honeycomb:    # N번 벌집이 몇번째 방에 있는지
    honeycomb += 6*cnt  # 방의 증가식 - 벌집의 개수가 6개 곱하기 방의 개수만큼 늘어난다.
    cnt += 1        # 방의 수를 1개씩 증가
print(cnt)