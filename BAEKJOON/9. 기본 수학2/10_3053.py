# 택시 기하학

'''
유클리드 기하학에서 원의 넓이
PI * r^2
택시 기하학에서 원의 넓이
2 * r^2
'''

# 풀이1
# 소수 6자리 까지 출력
import math

num = float(input())

# 유클리드 기하학에서 원의 넓이
def euclideanGeometry(n):                   # PI*r**2
    euclidean = math.pi * math.pow(n, 2)
    return euclidean
# 택시 기하학에서 원의 넓이
def taxicapGeometry(n):                     # 2*r**2
    taxicap = 2 * math.pow(n, 2)
    return taxicap

print('%.6f' % euclideanGeometry(num))
print('%.6f' % taxicapGeometry(num))

# 31312KB 76ms