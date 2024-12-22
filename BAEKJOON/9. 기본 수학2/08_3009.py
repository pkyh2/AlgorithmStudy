# 네 번째 점

'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''

# 풀이1
X = []
Y = []
result = []
for i in range(3):
    x, y = map(int, input().split())
    X.append(x)             # [5, 5, 7]
    Y.append(y)             # [5, 7, 5]

if X.count(max(X)) > 1:     # 최대값이 1개보다 많으면 최소값 출력
    result.append(min(X))
else:
    result.append(max(X))

if Y.count(max(Y)) > 1:
    result.append(min(Y))
else:
    result.append(max(Y))


print(' '.join(map(str, result)))
